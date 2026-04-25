# 🌀 NexusFrame — Quantum AI Video Factory v2.5

[English] | [Русский](README.RU.md)

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Sora Migration](https://img.shields.io/badge/Sora-Migration%20Layer-orange)](https://github.com/homgorn/nexusframe-ai-factory)
[![Compliance](https://img.shields.io/badge/Compliance-C2PA%20Signed-green)](https://c2pa.org/)

**NexusFrame** is an autonomous AI-driven factory for creating high-end real estate video advertisements. It serves as a drop-in replacement for OpenAI Sora, orchestrating multiple SOTA engines for aesthetic supremacy.

---

## 🚀 Quick Start

### 1. Prerequisites
**macOS:**
```bash
brew install docker python3 node ffmpeg
```

### 2. Set up API Keys
Edit your `.env` file and add your keys:
*   **OpenAI/Claude:** For Aura Intelligence brain.
*   **ComfyUI API:** For photorealistic generations.
*   **Arweave Key:** For permanent storage.

### 3. Launch the Symphony
```bash
# Make scripts executable
chmod +x scripts/*.sh

# Start the factory
./scripts/start.sh
```

### 4. Access the Control Center
*   **Quantum Dashboard:** `http://localhost:3000`
*   **API Docs:** `http://localhost:8000/docs`
*   **Landing Page:** [https://homgorn.github.io/nexusframe-ai-factory/](https://homgorn.github.io/nexusframe-ai-factory/)

---

## ✨ Features

### 🧠 Aura Intelligence
*   **Autonomous Research:** Scans Hugging Face for new LoRAs and styles.
*   **Aesthetic Scoring:** Rejects videos with scores below 8.5/10.

### 🎹 Multi-Engine Orchestration
*   **ComfyUI (FLUX.1):** Cinematic photorealism.
*   **Gaussian Splatting (3DGS):** Virtual DOP 3D property tours.
*   **Manim (v0.20):** Interactive property data & charts.
*   **Remotion (v4.0):** Frame-perfect React orchestration.

---

## 📖 Usage (API)

### Create a Production Run:
```bash
curl -X POST http://localhost:8000/api/parse-listing \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.cian.ru/sale/flat/123456/",
    "config": {
      "duration": 30,
      "quality": "1080p",
      "engine": "symphony-auto"
    }
  }'
```

---

## 📁 Project Structure
```text
nexusframe/
├── adapters/           # Engine adapters (Comfy, Manim, Remotion)
├── backend/            # FastAPI Quantum Orchestrator
├── frontend/           # Ultra-Premium Dashboard (Next.js)
├── scripts/            # Utility scripts (start, stop, logs)
├── index.html          # SEO Landing Page
└── README.md           # This file
```

---

## ⚖️ License
Licensed under the **Apache License, Version 2.0**.

*Made with ❤️ for the Post-Sora Era.*
