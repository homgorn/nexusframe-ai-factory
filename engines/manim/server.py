from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
import uuid
import logging

app = FastAPI()
logger = logging.getLogger("manim-engine")

OUTPUT_DIR = "/app/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class RenderRequest(BaseModel):
    job_id: str
    images: list[str] = []
    title: str = ""
    price: str = ""
    address: str = ""

@app.post("/render")
async def render_video(req: RenderRequest):
    if not req.job_id:
        raise HTTPException(status_code=400, detail="job_id is required")
        
    output_filename = f"manim_{req.job_id}.mp4"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    logger.info(f"Starting Manim render for job {req.job_id}")
    
    # In production, we would execute a specific Python Manim scene.
    # subprocess.run(["manim", "-qk", "-o", output_path, "scene.py", "RealEstateScene"])
    
    # Simulate work
    try:
        with open(output_path, "w") as f:
            f.write(f"Dummy Manim render for {req.job_id}")
            
        return {
            "success": True,
            "output_path": f"/outputs/{output_filename}",
            "engine": "manim"
        }
    except Exception as e:
        logger.error(f"Error rendering: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@app.get("/health")
def health():
    return {"status": "ok", "engine": "manim"}
