FROM python:3.11-slim

# Install system dependencies required by Manim (Cairo, LaTeX, FFmpeg)
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    libpango1.0-dev \
    ffmpeg \
    texlive \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-latex-recommended \
    texlive-science \
    tipa \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/engine

# Copy Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy server code
COPY server.py .

EXPOSE 8004

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8004"]
