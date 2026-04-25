"""
Video Factory — Adapter Layer
=============================
Isolates our core from vendor dependencies (Git Submodules).
Backend imports ONLY from this package, never from vendor/ directly.

Modules:
    - remotion_adapter:    React → MP4 (remotion-dev/remotion)
    - hyperframes_adapter: HTML+GSAP → MP4 (heygen-com/hyperframes)
    - manim_adapter:       Python → animated MP4 (ManimCommunity/manim)
    - digitalsamba_adapter: Voiceover, music, brands (digitalsamba/toolkit)
    - world3d_adapter:     Photos → 3D tour (Tencent HY-World 2.0)
    - agent_adapter:       AI orchestration (open-harness)
    - ffmpeg_adapter:      Post-processing (watermark, resize, encode)
"""
