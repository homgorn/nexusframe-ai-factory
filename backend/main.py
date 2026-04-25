from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Literal
from enum import Enum
import uuid
from datetime import datetime
import asyncio
from pathlib import Path
from sqlalchemy.orm import Session

from .database import engine, get_db, Base
from . import models

# Создаем таблицы при старте (для MVP, в продакшене лучше Alembic)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Real Estate Video Factory API", version="1.0.0")

# CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== SCHEMAS (Pydantic) ====================

class AspectRatio(str, Enum):
    HORIZONTAL = "16:9"
    VERTICAL = "9:16"
    SQUARE = "1:1"
    INSTAGRAM = "4:5"

class AIProvider(str, Enum):
    FFMPEG = "ffmpeg"
    HUNYUAN = "hunyuan"
    COGVIDEO = "cogvideo"
    KLING = "kling"
    RUNWAY = "runway"
    WAN = "wan"
    PIKA = "pika"

class MusicGenre(str, Enum):
    AMBIENT = "ambient"
    UPBEAT = "upbeat"
    CLASSICAL = "classical"
    ELECTRONIC = "electronic"
    NONE = "none"

class VideoConfigSchema(BaseModel):
    aspect_ratio: AspectRatio = AspectRatio.HORIZONTAL
    duration: int = 30
    quality: Literal["720p", "1080p", "4K"] = "1080p"
    fps: int = 30
    template: Literal["luxury", "modern", "minimal", "dynamic"] = "modern"
    
    # AI settings
    ai_provider: AIProvider = AIProvider.FFMPEG
    use_ai_video: bool = False
    enhance_images: bool = True
    
    # Voice & Audio
    generate_voiceover: bool = False
    voice: Literal["male", "female"] = "female"
    language: Literal["ru", "en"] = "ru"
    music_genre: MusicGenre = MusicGenre.AMBIENT
    music_volume: float = 0.3
    
    # Branding
    watermark: bool = True
    watermark_position: Literal["top-left", "top-right", "bottom-left", "bottom-right"] = "bottom-right"
    agency_name: Optional[str] = None
    
    # Text
    title_style: Literal["bold", "elegant"] = "bold"
    description_tone: Literal["formal", "casual", "luxury"] = "formal"
    show_price: bool = True
    cta: str = "Звоните сейчас!"
    
    # Platforms
    platforms: List[Literal["youtube", "instagram", "tiktok"]] = ["youtube"]

class ParseRequest(BaseModel):
    url: HttpUrl
    config: VideoConfigSchema = VideoConfigSchema()

class JobSchema(BaseModel):
    id: str
    status: models.JobStatus
    source: str
    progress: int
    created_at: datetime
    updated_at: datetime
    config: dict
    source_url: Optional[str] = None
    result_url: Optional[str] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True

# ==================== ENDPOINTS ====================

@app.post("/api/parse-listing", response_model=JobSchema)
async def parse_listing(request: ParseRequest, db: Session = Depends(get_db)):
    """Парсинг объявления по URL и создание видео"""
    
    job = models.Job(
        source="url",
        source_url=str(request.url),
        status=models.JobStatus.PENDING,
        config=request.config.dict()
    )
    
    db.add(job)
    db.commit()
    db.refresh(job)
    
    # Запуск Celery таски
    from .worker import process_video_job
    process_video_job.delay(job.id, job.config, job.source_url)
    
    return job

@app.get("/api/job/{job_id}", response_model=JobSchema)
async def get_job_status(job_id: str, db: Session = Depends(get_db)):
    """Получить статус задачи"""
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.get("/api/jobs", response_model=List[JobSchema])
async def list_jobs(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    """Список всех задач"""
    return db.query(models.Job).order_by(models.Job.created_at.desc()).offset(offset).limit(limit).all()

@app.get("/")
async def root():
    return {
        "name": "Real Estate Video Factory API",
        "version": "1.0.0",
        "status": "online",
        "database": "connected"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

