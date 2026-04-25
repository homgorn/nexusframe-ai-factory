# 🎬 Real Estate Video Factory

**Автоматическая фабрика для создания рекламных роликов недвижимости**

Парсинг объявлений → AI обработка → Генерация видео → Экспорт

---

## 🚀 Быстрый старт

### 1. Установите зависимости

**macOS:**
```bash
brew install docker python3 node ffmpeg
```

### 2. Настройте API ключи

Отредактируйте файл `.env` и добавьте ваши API ключи:
- OpenAI (опционально)
- Claude (опционально)
- Kling, Runway (платные, опционально)

### 3. Запустите проект

```bash
cd ~/Desktop/video-factory

# Сделать скрипты исполняемыми
chmod +x scripts/*.sh

# Запустить сервисы
./scripts/start.sh
```

### 4. Откройте приложение

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **MinIO Console**: http://localhost:9001 (minioadmin/minioadmin)

---

## ✨ Возможности

### Парсинг объявлений
- ✅ CIAN.ru
- ✅ Avito.ru  
- ✅ Yandex.Realty
- ✅ Domclick.ru

### AI Генерация
**Бесплатные:**
- FFmpeg (быстро, без AI)
- Google Colab (CogVideoX, HunyuanVideo)
- Kaggle Notebooks
- HuggingFace Spaces

**Платные:**
- Kling API ($6.99/month)
- Runway Gen-4 ($95/month)
- OpenAI Sora
- Google Veo

### Настройки видео
- 📐 Форматы: 16:9, 9:16, 1:1, 4:5
- 🎨 Качество: 720p, 1080p, 4K
- ⏱️ Длина: 15-90 секунд
- 🎵 Музыка: Ambient, Upbeat, Classical
- 🎙️ Озвучка: AI голоса (мужской/женский)
- 💬 Субтитры и водяные знаки

---

## 📖 Использование

### Через API

**Парсинг объявления:**
```bash
curl -X POST http://localhost:8000/api/parse-listing \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.cian.ru/sale/flat/123456/",
    "config": {
      "duration": 30,
      "quality": "1080p",
      "ai_provider": "ffmpeg"
    }
  }'
```

**Проверить статус:**
```bash
curl http://localhost:8000/api/job/{job_id}
```

---

## 🛠️ Команды

```bash
# Запуск всех сервисов
./scripts/start.sh

# Остановка
./scripts/stop.sh

# Просмотр логов
./scripts/logs.sh api
./scripts/logs.sh postgres

# Перезапуск
docker-compose restart api
```

---

## 📁 Структура проекта

```
video-factory/
├── backend/              # FastAPI приложение
│   ├── main.py          # Главный файл API
│   ├── requirements.txt # Python зависимости
│   └── Dockerfile       # Docker образ
├── frontend/            # React/Next.js (TODO)
├── scripts/             # Утилиты
│   ├── start.sh        # Запуск
│   ├── stop.sh         # Остановка
│   └── logs.sh         # Логи
├── uploads/             # Загруженные файлы
├── outputs/             # Готовые видео
├── temp/                # Временные файлы
├── docker-compose.yml   # Конфигурация сервисов
├── .env                 # Переменные окружения
└── README.md            # Документация
```

---

## 🔧 Настройка AI моделей

### Google Colab (бесплатно)

1. Откройте новый notebook: https://colab.research.google.com/
2. Установите ngrok и запустите сервер
3. Скопируйте URL ngrok в `.env` файл
4. API автоматически будет использовать Colab

### Платные API

Добавьте ключи в `.env`:
```bash
KLING_API_KEY=your_key
RUNWAY_API_KEY=your_key
```

---

## 📊 Мониторинг

- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **MinIO Console**: http://localhost:9001 (файловое хранилище)
- **Database**: PostgreSQL на порту 5432

---

## 🐛 Решение проблем

**Docker не запускается:**
```bash
# macOS
brew install --cask docker
open -a Docker

# Проверка
docker --version
docker-compose --version
```

**Порты заняты:**
```bash
# Проверить что использует порт 8000
lsof -i :8000

# Остановить процесс
kill -9 <PID>
```

**Нет прав на скрипты:**
```bash
chmod +x scripts/*.sh
```

---

## 📞 Поддержка

- 📖 Документация: http://localhost:8000/docs
- 🐛 Issues: GitHub Issues
- 💬 Вопросы: Telegram/Discord

---

## 📄 Лицензия

MIT License - свободное использование

---

**Made with ❤️ for real estate professionals**
