# 🧠 Claude Memory System - Architecture

> **Цель**: Эффективная память между чатами без потери контекста и с минимальным использованием токенов

---

## 📁 Структура `.claude-memory/`

```
.claude-memory/
├── README.md                    ← Ты здесь
├── MEMORY_INDEX.json           ← Индекс всех файлов памяти (быстрый поиск)
│
├── checkpoints/                 ← Снимки состояния после каждого checkpoint
│   ├── checkpoint_1.1_DONE.md
│   ├── checkpoint_1.2_DONE.md
│   └── ...
│
├── logs/                        ← Хронологические логи работы
│   ├── 2025-01-13_session_1.md
│   ├── 2025-01-14_session_2.md
│   └── ...
│
├── code-snapshots/              ← Полные копии кода после изменений
│   ├── backend_main_v1.py
│   ├── backend_main_v2.py
│   ├── cian_parser_v1.py
│   └── ...
│
└── context/                     ← Сжатый контекст для быстрой загрузки
    ├── current_state.json       ← Текущее состояние (JSON, 1-2KB)
    ├── last_10_changes.md       ← Последние 10 изменений (краткие)
    └── active_files.txt         ← Список файлов в работе
```

---

## 🎯 Система работает так:

### 1️⃣ **В начале чата** (Claude читает):
```
1. current_state.json (быстро, 2KB)
2. last_10_changes.md (последние действия)
3. MASTER_STATUS.md (полный статус)
```

**Итого**: ~5-10KB текста вместо чтения всего проекта

### 2️⃣ **Во время работы** (Claude пишет):
```
- Лог в logs/YYYY-MM-DD_session_N.md
- Изменённый код в code-snapshots/
```

### 3️⃣ **После checkpoint** (Claude создаёт):
```
- checkpoints/checkpoint_X.Y_DONE.md
  ├── Что сделано
  ├── Код который был написан
  ├── Проблемы найденные
  └── Следующий шаг
```

### 4️⃣ **В конце сессии** (Claude обновляет):
```
- current_state.json
- last_10_changes.md
- MEMORY_INDEX.json
```

---

## 💾 MEMORY_INDEX.json

Быстрый индекс всех файлов для поиска:

```json
{
  "version": "1.0",
  "last_updated": "2025-01-13T20:30:00Z",
  "total_checkpoints": 3,
  "total_sessions": 5,
  "total_code_files": 12,
  
  "checkpoints": [
    {
      "id": "1.1",
      "name": "CIAN Parser",
      "status": "completed",
      "file": "checkpoints/checkpoint_1.1_DONE.md",
      "date": "2025-01-13",
      "files_created": ["backend/parsers/cian_parser.py"],
      "lines_of_code": 150,
      "keywords": ["parser", "cian", "playwright", "scraping"]
    }
  ],
  
  "code_files": [
    {
      "path": "backend/parsers/cian_parser.py",
      "versions": ["v1", "v2", "v3"],
      "latest": "code-snapshots/cian_parser_v3.py",
      "last_modified": "2025-01-13",
      "description": "CIAN парсер с Playwright",
      "keywords": ["parser", "async", "playwright"]
    }
  ],
  
  "recent_changes": [
    {
      "date": "2025-01-13",
      "session": "session_1",
      "summary": "Создан CIAN парсер",
      "files": ["cian_parser.py"],
      "checkpoint": "1.1"
    }
  ]
}
```

---

## 📝 Формат checkpoint файла

**Пример**: `checkpoints/checkpoint_1.1_DONE.md`

```markdown
# ✅ Checkpoint 1.1 - CIAN Parser COMPLETED

**Дата**: 2025-01-13
**Токены использовано**: 15,000
**Время работы**: 2 часа

---

## 🎯 Что сделано

- [x] Создан файл `backend/parsers/cian_parser.py`
- [x] Функция `parse_cian(url)` работает
- [x] Парсинг title, price, images, address
- [x] Error handling добавлен
- [x] Тесты пройдены

---

## 💻 Код который был написан

### Файл: backend/parsers/cian_parser.py

\`\`\`python
# ПОЛНЫЙ код файла здесь (для быстрого восстановления)
async def parse_cian(url: str) -> dict:
    async with async_playwright() as p:
        # ... весь код ...
\`\`\`

**Версия**: v1
**Строк кода**: 150
**Snapshot**: code-snapshots/cian_parser_v1.py

---

## 🐛 Проблемы найденные

1. Playwright требует дополнительную установку браузеров
   - Решение: `playwright install chromium`

2. CIAN блокирует по User-Agent
   - Решение: Добавлен реалистичный User-Agent

---

## ✅ Критерий готовности выполнен

```python
# Тест прошёл
data = await parse_cian("https://cian.ru/...")
assert data['title'] is not None
assert len(data['images']) > 0
```

---

## 🚀 Следующий шаг

**Checkpoint 1.2**: FFmpeg Video Generation
- Создать `backend/video/ffmpeg_generator.py`
- Ken Burns эффект
- Музыка overlay
```

---

## 📊 Формат лога сессии

**Пример**: `logs/2025-01-13_session_1.md`

```markdown
# 📅 Session Log - 2025-01-13 #1

**Время начала**: 14:30
**Время окончания**: 16:45
**Длительность**: 2h 15min
**Токены использовано**: 15,000

---

## 🎯 Цель сессии
Создать CIAN парсер (Checkpoint 1.1)

---

## ⚡ Действия

### 14:30 - Начало
- Прочитал MASTER_STATUS.md
- Понял текущий checkpoint: 1.1

### 14:45 - Установка зависимостей
```bash
pip install playwright
playwright install chromium
```

### 15:00 - Создание парсера
- Создан файл `cian_parser.py`
- Написана основная функция

### 15:30 - Тестирование
- Тест на реальном URL
- Нашли проблему с User-Agent
- Исправили

### 16:00 - Финализация
- Добавлен error handling
- Создан snapshot кода
- Обновлён MASTER_STATUS.md

### 16:45 - Завершение
- Checkpoint 1.1 DONE ✅
- Создан checkpoint файл

---

## 📦 Файлы созданные/изменённые

- [NEW] backend/parsers/__init__.py
- [NEW] backend/parsers/cian_parser.py
- [EDIT] backend/main.py (добавлен import)
- [EDIT] MASTER_STATUS.md (checkpoint 1.1 → ✅)

---

## 🔍 Ключевые находки

1. Playwright медленный (~3 сек на страницу)
   - Можно ускорить отключением изображений
   
2. CIAN иногда возвращает 403
   - Нужен retry механизм

---

## 🧠 Контекст для следующего чата

**Закончили на**: Checkpoint 1.1 готов
**Следующее**: Checkpoint 1.2 - FFmpeg
**Активные файлы**: cian_parser.py работает
**Проблемы**: Нет критичных
```

---

## 🔄 Автоматическое обновление

### В конце каждой сессии Claude автоматически:

1. **Создаёт лог** в `logs/`
2. **Обновляет `current_state.json`**:
```json
{
  "current_checkpoint": "1.2",
  "last_session": "2025-01-13_session_1",
  "active_files": ["backend/video/ffmpeg_generator.py"],
  "next_action": "Создать FFmpeg wrapper",
  "progress": 25
}
```

3. **Обновляет `last_10_changes.md`**:
```markdown
1. [2025-01-13 16:45] ✅ Checkpoint 1.1 done - CIAN parser
2. [2025-01-13 14:30] Started work on CIAN parser
3. [2025-01-13 12:00] Created project structure
...
```

4. **Обновляет `MEMORY_INDEX.json`** с новыми файлами

---

## 🎯 Преимущества системы

### ✅ Экономия токенов:
- Читать 5-10KB контекста вместо всего проекта
- current_state.json = ~2KB (мгновенная загрузка)
- last_10_changes.md = ~3KB (последние действия)

### ✅ Быстрое восстановление:
- Claude читает checkpoint → видит полный код
- Не нужно переписывать с нуля
- Copy-paste из checkpoint файла

### ✅ История изменений:
- Каждая версия кода сохранена
- Можно откатиться к любой версии
- Логи показывают что и когда делалось

### ✅ Поиск по контексту:
- MEMORY_INDEX.json - быстрый поиск
- Keywords для каждого файла
- Можно найти "где мы делали парсер"

---

## 🚀 Как использовать в новом чате

```
Привет! Проект Real Estate Video Factory
Путь: ~/Desktop/video-factory

Прочитай в этом порядке:
1. .claude-memory/context/current_state.json
2. .claude-memory/context/last_10_changes.md
3. MASTER_STATUS.md

Продолжаем работу!
```

Claude загрузит контекст за 5-10 секунд вместо минуты!

---

## 🔧 Дополнительные фичи

### 1. Diff tracking
```
code-snapshots/
  ├── cian_parser_v1.py
  ├── cian_parser_v2.py
  └── cian_parser_v1_to_v2.diff  ← Что изменилось
```

### 2. Code embeddings (опционально)
Если нужен векторный поиск:
```python
# Создать embeddings через OpenAI API
embeddings/
  └── code_embeddings.json  ← Векторы для поиска
```

### 3. Automatic changelog
```
CHANGELOG.md ← Генерируется автоматически из логов
```

---

## 📊 Метрики

Система автоматически трекает:
- Токены использованные по сессиям
- Время работы
- Строки кода написанные
- Количество checkpoints
- Скорость разработки (checkpoints/день)

---

**Создано для максимальной эффективности работы с Claude! 🧠**
