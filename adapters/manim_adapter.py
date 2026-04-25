"""
Manim Adapter — Python → Animated MP4 (3Blue1Brown style).
Wraps ManimCommunity/manim. MIT License.
Use for infographics, price charts, floor plan animations.
"""
import asyncio
import tempfile
from pathlib import Path
from typing import Dict, Any

from .base import BaseVideoAdapter, VideoRequest, VideoResult, EngineType


class ManimAdapter(BaseVideoAdapter):
    """Generate animated infographic videos using Manim CE."""
    
    engine_type = EngineType.MANIM
    
    def __init__(self, manim_path: str = "manim"):
        self.manim_path = manim_path
    
    async def generate(self, request: VideoRequest) -> VideoResult:
        """Generate an animated infographic for a property listing."""
        try:
            output_dir = Path(request.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{request.job_id}.mp4"
            
            # Generate Manim scene Python file
            scene_code = self._generate_scene(request)
            scene_file = output_dir / f"{request.job_id}_scene.py"
            scene_file.write_text(scene_code, encoding="utf-8")
            
            quality_flag = {
                "720p": "-ql",    # low quality (720p)
                "1080p": "-qm",  # medium quality (1080p)
                "4K": "-qh",     # high quality (4K)
            }.get(request.quality, "-qm")
            
            cmd = [
                self.manim_path, "render",
                quality_flag,
                str(scene_file),
                "PropertyScene",
                "-o", str(output_path),
            ]
            
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
                    error=f"Manim render failed: {stderr.decode()[:500]}"
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
    
    def _generate_scene(self, request: VideoRequest) -> str:
        """Generate a Manim scene for property infographics."""
        return f'''
from manim import *

class PropertyScene(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#0a0a0f"
        
        # Title with gradient effect
        title = Text("{request.title or 'Premium Property'}", 
                     font_size=56, color=WHITE, font="Inter")
        title.to_edge(UP, buff=0.8)
        
        # Price badge
        price_bg = RoundedRectangle(
            corner_radius=0.2, width=6, height=1.2,
            fill_color="#7c3aed", fill_opacity=1, stroke_width=0
        )
        price_text = Text("{request.price or '---'}", 
                         font_size=48, color=WHITE, weight=BOLD)
        price_group = VGroup(price_bg, price_text).arrange(ORIGIN)
        price_group.next_to(title, DOWN, buff=0.5)
        
        # Property details
        details = [
            ("📍", "{request.address or 'Адрес'}"),
            ("📐", "{request.area or 'Площадь'}"),
            ("🏠", "{request.rooms or 'Комнаты'}"),
        ]
        
        detail_texts = VGroup()
        for icon, text in details:
            line = Text(f"{{icon}}  {{text}}", font_size=28, color=GRAY_A)
            detail_texts.add(line)
        
        detail_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        detail_texts.next_to(price_group, DOWN, buff=0.8)
        
        # Animations
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(price_group, shift=UP * 0.3), run_time=1)
        
        for detail in detail_texts:
            self.play(FadeIn(detail, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(2)
        
        # Agency branding
        agency = Text("{request.agency_name or ''}", 
                     font_size=20, color=GRAY_B)
        agency.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(agency), run_time=0.5)
        self.wait(1)
'''
    
    async def check_health(self) -> bool:
        try:
            proc = await asyncio.create_subprocess_exec(
                self.manim_path, "--version",
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            await proc.communicate()
            return proc.returncode == 0
        except Exception:
            return False
    
    def get_capabilities(self) -> Dict[str, Any]:
        return {
            "engine": "manim",
            "max_duration": 120,
            "formats": ["mp4", "gif", "png_sequence"],
            "features": [
                "mathematical_animations", "infographics",
                "price_charts", "floor_plan_animation",
                "3blue1brown_style", "text_animations"
            ],
            "gpu_required": False,
            "license": "MIT (fully free)"
        }
