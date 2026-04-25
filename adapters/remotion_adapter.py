"""
Remotion Adapter — React → MP4 video generation.
Wraps remotion-dev/remotion CLI and digitalsamba toolkit patterns.
"""
import asyncio
import json
from pathlib import Path
from typing import Dict, Any

from .base import BaseVideoAdapter, VideoRequest, VideoResult, EngineType


class RemotionAdapter(BaseVideoAdapter):
    """Generate videos using Remotion (React → MP4)."""
    
    engine_type = EngineType.REMOTION
    
    def __init__(self, remotion_project_dir: str = "./vendor/digitalsamba-toolkit"):
        self.project_dir = Path(remotion_project_dir)
    
    async def generate(self, request: VideoRequest) -> VideoResult:
        """Generate video by calling the Remotion Engine microservice."""
        try:
            import os
            import aiohttp
            
            api_url = os.getenv("REMOTION_API_URL", "http://localhost:8001")
            
            payload = {
                "job_id": request.job_id,
                "images": request.images,
                "title": request.title,
                "description": request.description,
                "price": request.price,
                "address": request.address,
                "template": request.template,
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{api_url}/render", json=payload) as resp:
                    if resp.status != 200:
                        error_text = await resp.text()
                        return VideoResult(
                            job_id=request.job_id,
                            success=False,
                            engine_used=self.engine_type,
                            error=f"Remotion Engine HTTP {resp.status}: {error_text}"
                        )
                        
                    data = await resp.json()
                    
                    if data.get("success"):
                        return VideoResult(
                            job_id=request.job_id,
                            success=True,
                            output_path=data.get("output_path"),
                            file_size_bytes=0, # We don't have the size immediately over HTTP
                            engine_used=self.engine_type,
                        )
                    else:
                        return VideoResult(
                            job_id=request.job_id,
                            success=False,
                            engine_used=self.engine_type,
                            error=data.get("error", "Unknown Remotion Engine error")
                        )
            
        except Exception as e:
            return VideoResult(
                job_id=request.job_id,
                success=False,
                engine_used=self.engine_type,
                error=f"Failed to connect to Remotion Engine: {str(e)}"
            )
    
    async def check_health(self) -> bool:
        """Check if Remotion CLI is available."""
        try:
            proc = await asyncio.create_subprocess_exec(
                "npx", "remotion", "--version",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await proc.communicate()
            return proc.returncode == 0
        except Exception:
            return False
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "engine": "remotion",
            "max_duration": 300,
            "formats": ["mp4", "webm", "gif"],
            "features": [
                "react_compositions", "ken_burns", "text_overlays",
                "branded_intros", "scene_transitions", "spring_animations",
                "digitalsamba_components", "remotion_studio_preview"
            ],
            "gpu_required": False,
            "license": "Remotion License (free for personal/small teams)"
        }
