import os
import asyncio
from celery import Celery
from sqlalchemy.orm import Session
from pathlib import Path

from .database import SessionLocal
from .models import Job, JobStatus, EngineType

# Add parent directory to path so we can import adapters
import sys
sys.path.append(str(Path(__file__).parent.parent))

from adapters.ffmpeg_adapter import FFmpegAdapter
from adapters.remotion_adapter import RemotionAdapter
from adapters.hyperframes_adapter import HyperFramesAdapter
from adapters.manim_adapter import ManimAdapter
from adapters.base import VideoRequest

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "video_factory",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

def update_job_status(db: Session, job_id: str, status: JobStatus, progress: int = None, error: str = None, result_url: str = None):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return
    
    job.status = status
    if progress is not None:
        job.progress = progress
    if error is not None:
        job.error = error
    if result_url is not None:
        job.result_url = result_url
        
    db.commit()

async def async_process_video(job_id: str, config: dict, source_url: str):
    db = SessionLocal()
    try:
        update_job_status(db, job_id, JobStatus.PROCESSING, progress=10)
        
        # 1. Parsing Phase
        from .parser import ListingParser
        
        update_job_status(db, job_id, JobStatus.PARSING, progress=20)
        
        if source_url and source_url.startswith("http"):
            try:
                parsed_data = await ListingParser.parse(source_url)
                
                images = parsed_data.get("images", [])
                if not images:
                    # Fallback if parser fails to find images
                    images = [
                        "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=80",
                        "https://images.unsplash.com/photo-1600607687931-cebf004f560c?w=1920&q=80",
                    ]
                
                title = parsed_data.get("title", "Luxury Modern Property")
                price = parsed_data.get("price", "Цена по запросу")
                address = parsed_data.get("address", "Адрес не указан")
                area = parsed_data.get("area", "")
                rooms = parsed_data.get("rooms", "")
            except Exception as e:
                # Fallback on parser error
                images = [
                    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=80",
                    "https://images.unsplash.com/photo-1600607687931-cebf004f560c?w=1920&q=80",
                ]
                title = "Parse Error Fallback"
                price = "$1,000,000"
                address = "Unknown"
                area = "Unknown"
                rooms = "Unknown"
        else:
            # Fallback for empty or invalid URL
            images = [
                "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=80",
                "https://images.unsplash.com/photo-1600607687931-cebf004f560c?w=1920&q=80",
                "https://images.unsplash.com/photo-1600607687644-aac4c156628c?w=1920&q=80",
            ]
            title = "Luxury Modern Villa"
            price = "$2,450,000"
            address = "Beverly Hills, CA"
            area = "450 sq.m."
            rooms = "5 beds, 4 baths"
        
        update_job_status(db, job_id, JobStatus.GENERATING, progress=40)
        
        # 2. Generation Phase
        engine_type = config.get("ai_provider", "ffmpeg")
        
        request = VideoRequest(
            job_id=job_id,
            images=images,
            title=title,
            price=price,
            address=address,
            area=area,
            rooms=rooms,
            duration=config.get("duration", 30),
            quality=config.get("quality", "1080p"),
            template=config.get("template", "modern"),
            output_dir="./output/videos"
        )
        
        # Select adapter
        if engine_type == EngineType.REMOTION.value:
            adapter = RemotionAdapter()
        elif engine_type == EngineType.HYPERFRAMES.value:
            adapter = HyperFramesAdapter()
        elif engine_type == EngineType.MANIM.value:
            adapter = ManimAdapter()
        else:
            adapter = FFmpegAdapter()
            
        result = await adapter.generate(request)
        
        if result.success:
            update_job_status(db, job_id, JobStatus.COMPLETED, progress=100, result_url=result.output_path)
        else:
            update_job_status(db, job_id, JobStatus.FAILED, error=result.error)

    except Exception as e:
        update_job_status(db, job_id, JobStatus.FAILED, error=str(e))
    finally:
        db.close()

@celery_app.task(name="process_video_job")
def process_video_job(job_id: str, config: dict, source_url: str):
    """Celery task entry point. Runs the async video processing pipeline."""
    asyncio.run(async_process_video(job_id, config, source_url))

