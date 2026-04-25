# 🌀 NexusFrame — Квантовая ИИ-Фабрика Видео v2.5

[English](README.md) | [Русский]

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Sora Migration](https://img.shields.io/badge/Sora-Migration%20Layer-orange)](https://github.com/homgorn/nexusframe-ai-factory)
[![Compliance](https://img.shields.io/badge/Compliance-C2PA%20Signed-green)](https://c2pa.org/)

**NexusFrame** — это автономная ИИ-фабрика для создания высококлассных рекламных роликов недвижимости. Система служит полноценной заменой OpenAI Sora, оркестрируя лучшие ИИ-движки для достижения эстетического превосходства.

---

## 🚀 Быстрый старт

### 1. Подготовка
**macOS:**
```bash
brew install docker python3 node ffmpeg
```

### 2. Настройка API ключей
Отредактируйте файл `.env` и добавьте ваши ключи:
*   **OpenAI/Claude:** Для мозга Aura Intelligence.
*   **ComfyUI API:** Для фотореалистичной генерации.
*   **Arweave Key:** Для вечного хранения видео.

### 3. Запуск Симфонии
```bash
# Сделать скрипты исполняемыми
chmod +x scripts/*.sh

# Запустить фабрику
./scripts/start.sh
```

### 4. Откройте приложение
*   **Quantum Dashboard:** `http://localhost:3000` (Панель управления)
*   **API Docs:** `http://localhost:8000/docs` (Swagger UI)
*   **Landing Page:** [https://homgorn.github.io/nexusframe-ai-factory/](https://homgorn.github.io/nexusframe-ai-factory/)

---

## ✨ Возможности

### 🧠 Интеллект Aura
*   **Автономный поиск:** Сканирует Hugging Face на наличие новых LoRA и стилей.
*   **Эстетическая оценка:** Бракует видео с оценкой ниже 8.5/10.

### 🎹 Мульти-движковая оркестрация
*   **ComfyUI (FLUX.1):** Кинематографический фотореализм.
*   **Gaussian Splatting (3DGS):** 3D-туры «Virtual DOP» из обычных фото.
*   **Manim (v0.20):** Инфографика и графики цен на недвижимость.
*   **Remotion (v4.0):** Точный React-монтаж.

---

## 📖 Использование (API)

### Создать задачу на генерацию:
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

## 📁 Структура проекта
```text
nexusframe/
├── adapters/           # Адаптеры движков (Comfy, Manim, Remotion)
├── backend/            # Квантовый оркестратор на FastAPI
├── frontend/           # Ультра-премиальный дашборд (Next.js)
├── scripts/            # Скрипты управления (start, stop, logs)
├── index.html          # SEO-лендинг
└── README.md           # Документация
```

---

## ⚖️ Лицензия
Лицензировано под **Apache License, Version 2.0**.

*Создано с ❤️ для эпохи после Sora.*
