# ✅ TODO List - Real Estate Video Factory

> Конкретные задачи для выполнения. Отмечай ✅ когда сделано!

---

## 🔥 ГОРЯЩИЕ ЗАДАЧИ (Сейчас)

### Checkpoint 1.1: CIAN Парсер
- [ ] Установить Playwright: `cd backend && source venv/bin/activate && pip install playwright && playwright install`
- [ ] Создать папку `backend/parsers/`
- [ ] Создать файл `backend/parsers/__init__.py`
- [ ] Создать файл `backend/parsers/cian_parser.py` с функцией:
  ```python
  async def parse_cian(url: str) -> dict:
      # Парсинг title, price, description, images, address
      return {...}
  ```
- [ ] Написать тест на реальном CIAN URL
- [ ] Добавить error handling (неверный URL, 404, блокировка)
- [ ] Интегрировать в `backend/main.py` endpoint `/api/parse-listing`

**Критерий готовности**: Реальный CIAN URL → получаем данные квартиры

---

## ⏰ СЛЕДУЮЩИЕ ЗАДАЧИ (После парсера)

### Checkpoint 1.2: FFmpeg Video Generation
- [ ] Создать папку `backend/video/`
- [ ] Создать `backend/video/ffmpeg_generator.py`
- [ ] Функция `generate_video_ffmpeg(images: List[str], config: VideoConfig) -> str`
- [ ] Ken Burns эффект (zoom + pan)
- [ ] Fade переходы между фото
- [ ] Добавление музыки (overlay)
- [ ] Субтитры (hardcoded через ffmpeg)
- [ ] Export в разных форматах (16:9, 9:16, 1:1)
- [ ] Тест: 5 фото → 30 сек видео

**Критерий готовности**: Список фото → MP4 видео с эффектами

---

### Checkpoint 1.3: Celery Integration
- [ ] Создать `backend/tasks.py`
- [ ] Setup Celery app с Redis
- [ ] Task: `parse_listing_task(url: str)`
- [ ] Task: `generate_video_task(job_id: str, images: List, config: dict)`
- [ ] Task: `full_pipeline_task(url: str, config: dict)` - парсинг + видео
- [ ] Progress tracking через Celery state
- [ ] Интеграция с FastAPI endpoints
- [ ] Тест: Запуск через `.delay()`

**Критерий готовности**: Async обработка работает, можно трекать прогресс

---

### Checkpoint 1.4: Database Models
- [ ] Создать `backend/models.py`
- [ ] SQLAlchemy Base
- [ ] Model: `Job` (id, status, url, config, result_url, progress, timestamps)
- [ ] Model: `User` (для будущего auth)
- [ ] Создать `backend/database.py` с connection
- [ ] Alembic setup: `alembic init alembic`
- [ ] Первая миграция: `alembic revision --autogenerate -m "Initial"`
- [ ] Применить: `alembic upgrade head`
- [ ] Обновить endpoints для сохранения в DB

**Критерий готовности**: Jobs сохраняются в PostgreSQL

---

### Checkpoint 1.5: Frontend Basic
- [ ] `cd frontend && npx create-next-app@latest . --typescript --tailwind --app`
- [ ] Создать компонент `VideoJobForm` (URL input + submit)
- [ ] API client: `lib/api.ts` с fetch функциями
- [ ] Компонент `JobsList` - список активных задач
- [ ] Компонент `JobStatus` - прогресс бар + статус
- [ ] Real-time updates (polling каждые 2 секунды)
- [ ] Download button для готовых видео

**Критерий готовности**: UI работает, можно создать и скачать видео

---

## 🎨 ДОПОЛНИТЕЛЬНЫЕ ЗАДАЧИ (После MVP)

### AI Text Enhancement
- [ ] `backend/ai/text_generator.py`
- [ ] Интеграция Claude API для улучшения описаний
- [ ] Генерация SEO-заголовков
- [ ] Генерация хештегов
- [ ] Мультиязычность (RU/EN)

### AI Audio
- [ ] `backend/ai/audio_generator.py`
- [ ] ElevenLabs TTS интеграция
- [ ] Mubert музыка генерация
- [ ] Audio mixing

### 3D World Generation
- [ ] `backend/ai_workers/hunyuan3d.py`
- [ ] Интеграция Hunyuan3D World Model
- [ ] `backend/ai_workers/gaussian_splatting.py`
- [ ] SHARP/gsplat для 2D→3D
- [ ] Unreal Engine automation script

### Social Media Integration
- [ ] `backend/social/youtube.py` - YouTube API
- [ ] `backend/social/tiktok.py` - TikTok API
- [ ] `backend/social/instagram.py` - Meta Graph API
- [ ] `backend/social/scheduler.py` - Multi-platform scheduling

---

## 🐛 BUGS TO FIX

- [ ] В `backend/main.py` парсеры возвращают mock данные (заглушки)
- [ ] FFmpeg генерация - только `asyncio.sleep()`, нет реального кода
- [ ] Docker Compose не протестирован
- [ ] MinIO bucket не создается автоматически
- [ ] Frontend папка пустая

---

## 📝 DOCUMENTATION TO WRITE

- [ ] API документация (примеры curl команд)
- [ ] Deployment guide для production
- [ ] Видео-туториал "Как запустить проект"
- [ ] Troubleshooting guide

---

## 🧪 TESTS TO WRITE

- [ ] `tests/test_cian_parser.py`
- [ ] `tests/test_ffmpeg_generator.py`
- [ ] `tests/test_api_endpoints.py`
- [ ] `tests/test_celery_tasks.py`
- [ ] Integration test: Full pipeline end-to-end

---

## 💡 OPTIMIZATION IDEAS

- [ ] Кеширование парсинга (не парсить один URL дважды)
- [ ] Thumbnail preview до генерации видео
- [ ] Batch processing (несколько квартир → одно видео)
- [ ] Webhook notifications при готовности видео
- [ ] Admin panel для мониторинга

---

## 🎯 MVP CHECKLIST (Must have для запуска)

- [ ] ✅ CIAN парсер работает
- [ ] ✅ FFmpeg генерация работает
- [ ] ✅ Celery обработка работает
- [ ] ✅ Database сохраняет jobs
- [ ] ✅ Frontend UI функционален
- [ ] ✅ Docker stack запускается
- [ ] ✅ Можно показать demo инвестору

**Когда все ✅ - MVP готов!** 🎉

---

## 📅 TIME ESTIMATES

| Checkpoint | Оценка времени | Приоритет |
|------------|---------------|-----------|
| 1.1 CIAN Parser | 4-6 часов | 🔥 ВЫСОКИЙ |
| 1.2 FFmpeg Video | 6-8 часов | 🔥 ВЫСОКИЙ |
| 1.3 Celery | 4-6 часов | 🔥 ВЫСОКИЙ |
| 1.4 Database | 3-4 часа | ⚡ СРЕДНИЙ |
| 1.5 Frontend | 6-8 часов | ⚡ СРЕДНИЙ |
| **TOTAL MVP** | **2-3 дня** | - |

---

**📌 ПОМНИ**: Отмечай задачи как выполненные и обновляй MASTER_STATUS.md!
