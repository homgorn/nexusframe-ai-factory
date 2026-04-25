from sqlalchemy import Column, String, Integer, DateTime, Boolean, JSON, Enum as SQLEnum
from .database import Base
import enum
from datetime import datetime
import uuid

class JobStatus(str, enum.Enum):
    PENDING = "pending"
    PARSING = "parsing"
    PROCESSING = "processing"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"

class EngineType(str, enum.Enum):
    FFMPEG = "ffmpeg"
    REMOTION = "remotion"
    HYPERFRAMES = "hyperframes"
    MANIM = "manim"
    HY_WORLD_3D = "hy-world-3d"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    status = Column(SQLEnum(JobStatus), default=JobStatus.PENDING)
    engine_type = Column(SQLEnum(EngineType), default=EngineType.FFMPEG)
    source = Column(String)  # "url" or "manual"
    source_url = Column(String, nullable=True)
    progress = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Store VideoConfig as JSON for flexibility in MVP
    config = Column(JSON)
    
    result_url = Column(String, nullable=True)
    error = Column(String, nullable=True)
    files_count = Column(Integer, nullable=True)

