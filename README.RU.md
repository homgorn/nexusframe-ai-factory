# 🌀 NexusFrame — Квантовая ИИ-Фабрика Видео v2.5

[English](README.md) | [Русский]

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Sora Migration](https://img.shields.io/badge/Sora-Migration%20Layer-orange)](https://github.com/homgorn/nexusframe-ai-factory)

**NexusFrame** — это первая в мире автономная **Квантовая Фабрика Видео**. Система служит полноценной заменой OpenAI Sora (закрытой в апреле 2026 года), предоставляя агентный оркестратор, который превращает ссылки на объекты недвижимости в высококлассные кинематографические ролики.

---

## 🚀 Квантовая Симфония (Архитектура)

NexusFrame не просто «генерирует» видео, он дирижирует **Симфонией** лучших ИИ-движков для достижения эстетического превосходства:

*   **🧠 Мозг Aura:** Автономный агент, который ищет новые LoRA на Hugging Face и ежедневно проводит исследование рынка, чтобы фабрика всегда была на шаг впереди трендов.
*   **🎹 Оркестратор:** Автоматически выбирает лучший движок для каждого кадра:
    *   **ComfyUI (FLUX.1):** Для ультра-реалистичной генерации.
    *   **Gaussian Splatting:** Для создания 3D-туров «Virtual DOP» из обычных фото.
    *   **Manim (v0.20):** Для сложной инфографики и графиков цен.
    *   **Remotion (v4.0):** Для React-оркестрации и монтажа с точностью до кадра.
*   **👁️ Aesthetic Scorer:** Система оценки качества на базе Visual-LLM, которая бракует любые видео с оценкой ниже 8.5/10, запуская авто-генерацию с улучшенными параметрами.

---

## ⚡ Слой миграции с Sora

Перейдите с Sora на NexusFrame за 60 секунд. Мы предоставляем OpenAI-совместимый API:

```bash
curl https://api.nexusframe.io/v1/video/generations \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "prompt": "Luxury penthouse in Moscow with sunset view, cinematic drone shot",
    "model": "sora-1-migration"
  }'
```

---

## ⚖️ Юридическая чистота (Готовность к EU AI Act)

В 2026 году комплаенс — это обязательное условие.
*   **C2PA Manifests:** Каждое видео имеет криптографическую подпись с данными о происхождении.
*   **Квантовый архив:** Вечное хранение в децентрализованных сетях **Arweave (AO Protocol)** и **IPFS**.
*   **Content Guard:** Автоматическая изоляция 18+ контента и слои модерации.

---

## 📦 Быстрый старт

1. **Клонировать Империю:**
   ```bash
   git clone https://github.com/homgorn/nexusframe-ai-factory.git
   ```
2. **Запустить Симфонию:**
   ```bash
   docker-compose up -d
   ```
3. **Панель управления:**
   Откройте `http://localhost:3000` для доступа к **Квантовому Дашборду**.

---

## 📄 Лицензия
Лицензировано под **Apache License, Version 2.0**. См. [LICENSE](LICENSE) для подробностей.

*Copyright © 2026 NexusFrame AI. Создано для эпохи после Sora.*
