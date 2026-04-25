"""
HyperFrames Adapter — HTML + GSAP → MP4 video generation.
Wraps heygen-com/hyperframes CLI. Apache 2.0 (fully free alternative to Remotion).
"""
import asyncio
import json
from pathlib import Path
from typing import Dict, Any

from .base import BaseVideoAdapter, VideoRequest, VideoResult, EngineType


class HyperFramesAdapter(BaseVideoAdapter):
    """Generate videos using HyperFrames (HTML → MP4). Apache 2.0."""
    
    engine_type = EngineType.HYPERFRAMES
    
    def __init__(self, hyperframes_dir: str = "./vendor/hyperframes"):
        self.project_dir = Path(hyperframes_dir)
    
    async def generate(self, request: VideoRequest) -> VideoResult:
        """Generate video by creating an HTML composition and rendering via HyperFrames."""
        try:
            output_dir = Path(request.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{request.job_id}.mp4"
            
            # Generate HTML composition for this property
            html_content = self._generate_html_composition(request)
            comp_file = output_dir / f"{request.job_id}_comp.html"
            comp_file.write_text(html_content, encoding="utf-8")
            
            # Render via HyperFrames CLI
            cmd = [
                "npx", "hyperframes", "render",
                str(comp_file),
                "--output", str(output_path),
            ]
            
            process = await asyncio.create_subprocess_exec(
                *cmd,
                cwd=str(self.project_dir),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                return VideoResult(
                    job_id=request.job_id,
                    success=False,
                    engine_used=self.engine_type,
                    error=f"HyperFrames render failed: {stderr.decode()[:500]}"
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
    
    def _generate_html_composition(self, request: VideoRequest) -> str:
        """Generate an HTML composition for a real estate listing."""
        images_html = ""
        for i, img in enumerate(request.images[:8]):
            delay = i * 4
            images_html += f'''
            <div class="scene" data-duration="4" data-transition="crossfade">
                <img src="{img}" style="width:100%; height:100%; object-fit:cover;"
                     data-animate="kenburns" data-direction="{'in' if i % 2 == 0 else 'out'}" />
            </div>'''

        return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ width: 1920px; height: 1080px; overflow: hidden; background: #000; font-family: 'Inter', sans-serif; }}
        .scene {{ position: absolute; inset: 0; }}
        .overlay {{ position: absolute; bottom: 60px; left: 60px; right: 60px;
                    background: rgba(0,0,0,0.7); backdrop-filter: blur(20px);
                    border-radius: 16px; padding: 40px; color: white; }}
        .price {{ font-size: 48px; font-weight: 800; color: #a78bfa; }}
        .title {{ font-size: 28px; font-weight: 600; margin-top: 8px; }}
        .details {{ font-size: 20px; color: rgba(255,255,255,0.7); margin-top: 12px; }}
    </style>
</head>
<body data-fps="30" data-width="1920" data-height="1080">
    {images_html}
    
    <div class="overlay" data-animate="fadeInUp" data-delay="1">
        <div class="price">{request.price}</div>
        <div class="title">{request.title}</div>
        <div class="details">{request.address} • {request.area} • {request.rooms}</div>
    </div>
</body>
</html>'''
    
    async def check_health(self) -> bool:
        try:
            proc = await asyncio.create_subprocess_exec(
                "npx", "hyperframes", "--version",
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            await proc.communicate()
            return proc.returncode == 0
        except Exception:
            return False
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "engine": "hyperframes",
            "max_duration": 300,
            "formats": ["mp4", "webm"],
            "features": [
                "html_compositions", "gsap_animations", "ken_burns",
                "50+_catalog_blocks", "shader_transitions", "mcp_server",
                "ai_agent_friendly"
            ],
            "gpu_required": False,
            "license": "Apache 2.0 (fully free)"
        }
