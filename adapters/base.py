"""
Base adapter interface — all video engines implement this contract.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
from enum import Enum


class EngineType(str, Enum):
    """Available video generation engines."""
    REMOTION = "remotion"
    HYPERFRAMES = "hyperframes"
    MANIM = "manim"
    FFMPEG = "ffmpeg"
    HY_WORLD_3D = "hy-world-3d"


@dataclass
class VideoRequest:
    """Input for any video engine adapter."""
    job_id: str
    images: List[str]  # file paths or URLs
    title: str = ""
    description: str = ""
    price: str = ""
    address: str = ""
    area: str = ""
    rooms: str = ""
    
    # Engine settings
    engine: EngineType = EngineType.FFMPEG
    aspect_ratio: str = "16:9"
    duration: int = 30
    quality: str = "1080p"
    fps: int = 30
    template: str = "modern"
    
    # Audio
    voiceover: bool = False
    voice_lang: str = "ru"
    music_genre: str = "ambient"
    music_volume: float = 0.3
    
    # Branding
    watermark: bool = True
    brand_profile: Optional[str] = None
    agency_name: Optional[str] = None
    
    # Output
    output_dir: str = "./output"
    
    # Extra metadata
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class VideoResult:
    """Output from any video engine adapter."""
    job_id: str
    success: bool
    output_path: Optional[str] = None
    duration_seconds: float = 0.0
    file_size_bytes: int = 0
    engine_used: EngineType = EngineType.FFMPEG
    error: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseVideoAdapter(ABC):
    """Abstract base class for all video engine adapters."""
    
    engine_type: EngineType
    
    @abstractmethod
    async def generate(self, request: VideoRequest) -> VideoResult:
        """Generate video from the given request."""
        ...
    
    @abstractmethod
    async def check_health(self) -> bool:
        """Check if the engine is available and healthy."""
        ...
    
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """Return engine capabilities (max duration, formats, etc.)."""
        ...
