# 🎯 MASTER STATUS - Real Estate Video Factory

> **ВАЖНО**: Это единый файл статуса проекта для всех чатов с Claude.
> При начале нового чата - ПЕРВЫМ ДЕЛОМ прочитай этот файл!

---

## 📍 ТЕКУЩЕЕ СОСТОЯНИЕ ПРОЕКТА

**Дата последнего обновления**: 2025-01-13
**Путь к проекту**: `~/Desktop/video-factory`
**Активный чат**: Initial Setup Chat

---

## ✅ ЧТО УЖЕ СДЕЛАНО

### Инфраструктура (70% готово)
- [x] Создана базовая структура папок
- [x] Docker Compose файл создан
- [x] .env файл с конфигурацией
- [x] Backend skeleton (FastAPI) - `/backend/main.py`
- [x] Requirements.txt с зависимостями
- [x] README.md с документацией
- [x] Скрипты запуска/остановки в `/scripts/`
- [x] .gitignore файл

### Backend API (40% готово)
- [x] FastAPI структура с endpoints
- [x] Pydantic models для VideoConfig
- [x] CORS middleware
- [x] Базовые endpoints:
  - `/api/parse-listing` (заглушка)
  - `/api/upload-manual` (заглушка)
  - `/api/job/{id}` (заглушка)
  - `/api/jobs` (заглушка)
- [ ] **НЕТ реальной логики** - только структура!

### Что НЕ работает (критично)
- [ ] Парсеры (CIAN, Avito) - только TODO
- [ ] FFmpeg генерация - только симуляция
- [ ] Celery tasks - файл не создан
- [ ] Database - нет SQLAlchemy моделей
- [ ] Frontend - папка пустая
- [ ] Docker - Dockerfile'ы есть, но не протестированы

---

## 🎯 ROADMAP - ГДЕ МЫ НАХОДИМСЯ

### PHASE 0: Setup ✅ (ГОТОВО 90%)
- [x] Структура проекта
- [x] Docker compose
- [ ] **ОСТАЛОСЬ**: Протестировать запуск Docker stack

### PHASE 1: MVP - FFmpeg Pipeline ⏳ (НАЧАТО 10%)
**Текущий фокус**: Checkpoint 1.1 - CIAN парсер

#### Checkpoint 1.1: CIAN Парсер ❌ (0%)
- [ ] Установить Playwright
- [ ] Написать парсер функцию
- [ ] Тесты парсера
- [ ] Error handling

#### Checkpoint 1.2: FFmpeg Video ❌ (0%)
- [ ] FFmpeg wrapper
- [ ] Ken Burns эффект
- [ ] Fade переходы
- [ ] Музыка overlay

#### Checkpoint 1.3: Celery ❌ (0%)
- [ ] tasks.py файл
- [ ] Redis connection
- [ ] Job tracking

#### Checkpoint 1.4: Frontend ❌ (0%)
- [ ] Next.js setup
- [ ] API integration
- [ ] UI components

#### Checkpoint 1.5: Database ❌ (0%)
- [ ] SQLAlchemy models
- [ ] Alembic миграции
- [ ] MinIO setup

### PHASE 2-6: Не начато ⏸️

---

## 📋 СЛЕДУЮЩИЕ ШАГИ (Приоритет)

### ⚡ СЕЙЧАС НУЖНО СДЕЛАТЬ:

**1. Checkpoint 1.1 - Создать CIAN парсер** (ВЫСОКИЙ ПРИОРИТЕТ)
   - Файл: `/backend/parsers/cian_parser.py`
   - Функция: `async def parse_cian(url: str) -> dict`
   - Тест: Проверить на реальном URL

**2. Создать Celery tasks** (ВЫСОКИЙ ПРИОРИТЕТ)
   - Файл: `/backend/tasks.py`
   - Task: `parse_and_generate_video.delay(url)`

**3. FFmpeg wrapper** (ВЫСОКИЙ ПРИОРИТЕТ)
   - Файл: `/backend/video/ffmpeg_generator.py`
   - Функция: `generate_video_ffmpeg(images, config)`

**4. Database models** (СРЕДНИЙ ПРИОРИТЕТ)
   - Файл: `/backend/models.py`
   - SQLAlchemy Job, User models

**5. Frontend setup** (НИЗКИЙ ПРИОРИТЕТ)
   - Next.js в `/frontend/`
   - Пока можно использовать API через Postman/curl

---

## 🔧 ТЕХНИЧЕСКИЙ СТЕК (Финальный)

### Confirmed Stack:
- **Backend**: FastAPI + Celery + Redis
- **Frontend**: Next.js 14 + TailwindCSS
- **Database**: PostgreSQL + SQLAlchemy
- **Storage**: MinIO (S3-compatible)
- **Video Processing**:
  - Phase 1: FFmpeg (быстро)
  - Phase 2: HunyuanVideo/CogVideoX (Colab/Kaggle)
  - Phase 3: Hunyuan3D + Gaussian Splatting + Unreal Engine 5
- **AI Services**:
  - Text: Claude/GPT
  - Audio: ElevenLabs/Azure TTS
  - Music: Mubert API
  - Image: Real-ESRGAN

### Отложено в roadmap:
- ~~Remotion~~ (в roadmap, но не в MVP из-за лицензии)

---

## 📦 ФАЙЛОВАЯ СТРУКТУРА

```
video-factory/
├── MASTER_STATUS.md          ← ТЫ ЗДЕСЬ! (читай первым делом)
├── ROADMAP.md                ← Полный roadmap с чекпоинтами
├── README.md                 ← Документация для пользователей
├── .env                      ← Конфигурация (API ключи)
├── docker-compose.yml        ← Docker services
├── .gitignore
│
├── backend/
│   ├── main.py              ✅ FastAPI app (структура готова)
│   ├── tasks.py             ❌ НЕ СОЗДАН (нужен!)
│   ├── models.py            ❌ НЕ СОЗДАН (нужен!)
│   ├── requirements.txt     ✅ Готов
│   ├── Dockerfile           ✅ Готов
│   │
│   ├── parsers/             ❌ ПАПКА НЕ СОЗДАНА
│   │   ├── __init__.py
│   │   ├── cian_parser.py   ← Checkpoint 1.1
│   │   ├── avito_parser.py
│   │   └── yandex_parser.py
│   │
│   ├── video/               ❌ ПАПКА НЕ СОЗДАНА
│   │   ├── __init__.py
│   │   ├── ffmpeg_generator.py  ← Checkpoint 1.2
│   │   └── ai_generators.py
│   │
│   ├── ai_workers/          ❌ ПАПКА НЕ СОЗДАНА
│   │   ├── __init__.py
│   │   ├── colab_worker.py
│   │   ├── hunyuan3d.py
│   │   └── gaussian_splatting.py
│   │
│   └── social/              ❌ ПАПКА НЕ СОЗДАНА (Phase 5)
│       ├── youtube.py
│       ├── tiktok.py
│       ├── instagram.py
│       └── scheduler.py
│
├── frontend/                ❌ ПУСТАЯ ПАПКА
│   └── (Next.js проект будет здесь)
│
├── scripts/
│   ├── start.sh            ✅ Готов
│   ├── stop.sh             ✅ Готов
│   └── quick-setup.sh      ✅ Готов
│
├── uploads/                ✅ Создана
├── outputs/                ✅ Создана
├── temp/                   ✅ Создана
└── assets/
    └── music/              ✅ Создана
```

---

## 🐛 ИЗВЕСТНЫЕ ПРОБЛЕМЫ

1. **Backend парсеры** - только заглушки, возвращают mock данные
2. **FFmpeg генерация** - только `asyncio.sleep()`, реальной генерации нет
3. **Frontend** - папка пустая
4. **Database** - нет моделей и миграций
5. **Docker** - не протестирован локально
6. **Celery** - tasks.py файл не создан

---

## 💡 ВАЖНЫЕ РЕШЕНИЯ

### Принятые решения:
1. ✅ **FFmpeg сначала** - для быстрого MVP
2. ✅ **3D как premium feature** - Hunyuan3D + Gaussian Splatting + Unreal
3. ✅ **Social media integration** - Phase 5 (YouTube, TikTok, Instagram, VK)
4. ✅ **AI content generation** - SEO, описания, хештеги автоматически
5. ✅ **Remotion в roadmap** - но не в MVP (лицензия Company $250/год)

### Открытые вопросы:
- [ ] Какие API ключи реально получить? (Claude, OpenAI, ElevenLabs?)
- [ ] Нужен ли Remotion или хватит FFmpeg?
- [ ] Colab vs Kaggle - что стабильнее?

---

## 📝 ИНСТРУКЦИЯ ДЛЯ НОВОГО ЧАТА

Когда начинаешь новый чат с Claude:

### 1. Первым делом прочитай этот файл:
```
Прочитай файл ~/Desktop/video-factory/MASTER_STATUS.md
```

### 2. Скажи Claude где проект:
```
Проект находится в ~/Desktop/video-factory
Продолжаем разработку Real Estate Video Factory
```

### 3. Узнай что делать дальше:
```
Смотри раздел "СЛЕДУЮЩИЕ ШАГИ" в MASTER_STATUS.md
Текущий приоритет: Checkpoint 1.1 - CIAN парсер
```

### 4. После работы - ОБНОВЛЯЙ ЭТОТ ФАЙЛ:
```
Обнови MASTER_STATUS.md:
- Отметь что сделал (✅)
- Добавь новые проблемы если нашел
- Обнови дату
```

---

## 🎯 КРИТЕРИИ ГОТОВНОСТИ MVP

### MVP готов когда:
- [ ] Можно вставить CIAN URL
- [ ] Автоматически парсится (title, price, images)
- [ ] Генерируется видео через FFmpeg
- [ ] Видео можно скачать
- [ ] Docker stack работает (`./scripts/start.sh`)
- [ ] 0 критических багов
- [ ] Можно показать demo

**Оценка времени до MVP**: 3-5 дней интенсивной работы

---

## 🔗 ПОЛЕЗНЫЕ ССЫЛКИ

- **ROADMAP полный**: `/ROADMAP.md` (читать для деталей)
- **API документация**: `http://localhost:8000/docs` (после запуска)
- **Frontend**: `http://localhost:3000` (когда будет)

---

## 📊 ПРОГРЕСС

```
PHASE 0 (Setup):        ████████████████░░  90%
PHASE 1 (MVP):          ██░░░░░░░░░░░░░░░░  10%
PHASE 2 (AI):           ░░░░░░░░░░░░░░░░░░   0%
PHASE 3 (3D):           ░░░░░░░░░░░░░░░░░░   0%
PHASE 4 (Advanced):     ░░░░░░░░░░░░░░░░░░   0%
PHASE 5 (Social):       ░░░░░░░░░░░░░░░░░░   0%
PHASE 6 (Production):   ░░░░░░░░░░░░░░░░░░   0%

ОБЩИЙ ПРОГРЕСС:         ███░░░░░░░░░░░░░░░  15%
```

---

## ✍️ CHANGELOG

### 2025-01-13
- ✅ Создан MASTER_STATUS.md
- ✅ Определена структура проекта
- ✅ Roadmap детализирован
- ⏳ Начат Checkpoint 1.1 (CIAN парсер)

---

**🔥 ПОМНИ**: Этот файл - источник правды. Всегда обновляй его после работы!
