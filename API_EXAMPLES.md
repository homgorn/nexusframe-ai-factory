# API Examples - Real Estate Video Factory

## 1. Парсинг объявления с CIAN

```bash
curl -X POST http://localhost:8000/api/parse-listing \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.cian.ru/sale/flat/123456/",
    "config": {
      "aspect_ratio": "16:9",
      "duration": 30,
      "quality": "1080p",
      "template": "modern",
      "ai_provider": "ffmpeg",
      "use_ai_video": false,
      "music_genre": "ambient",
      "watermark": true
    }
  }'
```

## 2. Получить статус задачи

```bash
curl http://localhost:8000/api/job/YOUR_JOB_ID
```

Response:
```json
{
  "id": "uuid-here",
  "status": "completed",
  "progress": 100,
  "result_url": "/outputs/uuid/video.mp4",
  "created_at": "2025-01-12T10:00:00",
  "config": {...}
}
```

## 3. Список всех задач

```bash
curl http://localhost:8000/api/jobs?limit=10
```

## 4. Разные форматы видео

### Вертикальное (TikTok, Reels)
```json
{
  "aspect_ratio": "9:16",
  "duration": 15,
  "platforms": ["tiktok", "instagram"]
}
```

### Квадратное (Instagram Feed)
```json
{
  "aspect_ratio": "1:1",
  "duration": 30
}
```

### 4K качество
```json
{
  "quality": "4K",
  "fps": 60
}
```

## 5. С AI генерацией (через Colab)

```json
{
  "ai_provider": "hunyuan",
  "use_ai_video": true,
  "enhance_images": true
}
```

## 6. С озвучкой и музыкой

```json
{
  "generate_voiceover": true,
  "voice": "female",
  "language": "ru",
  "music_genre": "upbeat",
  "music_volume": 0.5
}
```
