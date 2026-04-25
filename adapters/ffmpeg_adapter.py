"""
FFmpeg Adapter — Basic video generation using FFmpeg.
This is the default, always-available engine that requires no external services.
Patterns inspired by Claude-Code-Video-Toolkit.
"""
import subprocess
import asyncio
import shutil
from pathlib import Path
from typing import Dict, Any, List

from .base import BaseVideoAdapter, VideoRequest, VideoResult, EngineType


class FFmpegAdapter(BaseVideoAdapter):
    """Generate videos using FFmpeg (always available, no GPU needed)."""
    
    engine_type = EngineType.FFMPEG
    
    def __init__(self, ffmpeg_path: str = "ffmpeg"):
        self.ffmpeg_path = ffmpeg_path
    
    async def generate(self, request: VideoRequest) -> VideoResult:
        """Generate a Ken Burns slideshow video from images."""
        try:
            output_dir = Path(request.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{request.job_id}.mp4"
            
            # Build FFmpeg filter for Ken Burns with crossfade
            cmd = self._build_slideshow_command(
                images=request.images,
                output=str(output_path),
                duration_per_image=max(3, request.duration // max(len(request.images), 1)),
                fps=request.fps,
                resolution=self._quality_to_resolution(request.quality),
            )
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                return VideoResult(
                    job_id=request.job_id,
                    success=False,
                    engine_used=self.engine_type,
                    error=stderr.decode()[:500]
                )
            
            stat = output_path.stat()
            return VideoResult(
                job_id=request.job_id,
                success=True,
                output_path=str(output_path),
                file_size_bytes=stat.st_size,
                engine_used=self.engine_type,
            )
            
        except Exception as e:
            return VideoResult(
                job_id=request.job_id,
                success=False,
                engine_used=self.engine_type,
                error=str(e)
            )
    
    async def check_health(self) -> bool:
        """Check if FFmpeg is installed."""
        return shutil.which(self.ffmpeg_path) is not None
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "engine": "ffmpeg",
            "max_duration": 600,
            "formats": ["mp4", "webm", "mov"],
            "features": ["slideshow", "ken_burns", "watermark", "resize", "concat"],
            "gpu_required": False,
            "license": "LGPL/GPL"
        }
    
    def _quality_to_resolution(self, quality: str) -> str:
        return {"720p": "1280:720", "1080p": "1920:1080", "4K": "3840:2160"}.get(quality, "1920:1080")
    
    def _build_slideshow_command(
        self, images: List[str], output: str,
        duration_per_image: int = 5, fps: int = 30, resolution: str = "1920:1080"
    ) -> List[str]:
        """Build FFmpeg command for a Ken Burns slideshow with crossfade."""
        cmd = [self.ffmpeg_path, "-y"]
        
        # Input each image
        for img in images:
            cmd.extend(["-loop", "1", "-t", str(duration_per_image), "-i", img])
        
        if len(images) == 1:
            # Single image — zoom effect
            cmd.extend([
                "-vf", f"scale={resolution},zoompan=z='min(zoom+0.0015,1.5)':d={duration_per_image * fps}:s={resolution.replace(':', 'x')}",
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                output
            ])
        else:
            # Multiple images — crossfade between them
            n = len(images)
            filter_parts = []
            
            for i in range(n):
                filter_parts.append(
                    f"[{i}:v]scale={resolution}:force_original_aspect_ratio=decrease,"
                    f"pad={resolution}:(ow-iw)/2:(oh-ih)/2:color=black,"
                    f"setsar=1,fps={fps}[v{i}]"
                )
            
            # Concatenate
            concat_inputs = "".join(f"[v{i}]" for i in range(n))
            filter_parts.append(f"{concat_inputs}concat=n={n}:v=1:a=0[outv]")
            
            filter_complex = ";".join(filter_parts)
            cmd.extend([
                "-filter_complex", filter_complex,
                "-map", "[outv]",
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                "-preset", "fast", "-crf", "23",
                output
            ])
        
        return cmd


class FFmpegPostProcessor:
    """Post-processing operations using FFmpeg patterns from the toolkit."""
    
    def __init__(self, ffmpeg_path: str = "ffmpeg"):
        self.ffmpeg_path = ffmpeg_path
    
    async def add_watermark(self, video: str, logo: str, output: str,
                            position: str = "bottom-right", opacity: float = 0.7) -> str:
        """Add watermark/logo overlay to video."""
        pos_map = {
            "top-left": "10:10",
            "top-right": "W-w-10:10",
            "bottom-left": "10:H-h-10",
            "bottom-right": "W-w-10:H-h-10"
        }
        overlay_pos = pos_map.get(position, pos_map["bottom-right"])
        
        cmd = [
            self.ffmpeg_path, "-y",
            "-i", video, "-i", logo,
            "-filter_complex",
            f"[1:v]format=rgba,colorchannelmixer=aa={opacity}[wm];[0:v][wm]overlay={overlay_pos}",
            "-c:v", "libx264", "-c:a", "copy",
            output
        ]
        
        process = await asyncio.create_subprocess_exec(*cmd, stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return output
    
    async def resize(self, video: str, output: str, resolution: str = "1920:1080") -> str:
        """Resize video to target resolution."""
        cmd = [
            self.ffmpeg_path, "-y", "-i", video,
            "-vf", f"scale={resolution}:force_original_aspect_ratio=decrease,pad={resolution}:(ow-iw)/2:(oh-ih)/2",
            "-c:v", "libx264", "-c:a", "copy",
            output
        ]
        process = await asyncio.create_subprocess_exec(*cmd, stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return output
    
    async def add_audio(self, video: str, audio: str, output: str,
                        volume: float = 0.3) -> str:
        """Mix background audio into video."""
        cmd = [
            self.ffmpeg_path, "-y",
            "-i", video, "-i", audio,
            "-filter_complex", f"[1:a]volume={volume}[bg];[0:a][bg]amix=inputs=2:duration=first",
            "-c:v", "copy",
            output
        ]
        process = await asyncio.create_subprocess_exec(*cmd, stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return output
