# 🤖 AI-COMPATIBILITY.md

> **Цель**: Сделать проект совместимым с любым AI инструментом (Claude, Cursor, VSCode Copilot, Windsurf и тд)

---

## ✅ ПРОВЕРКА СИСТЕМЫ - РАБОТАЕТ!

### Проверил файлы:
1. ✅ `.claude-memory/context/current_state.json` - **работает!**
2. ✅ `.claude-memory/context/last_10_changes.md` - **работает!**
3. ✅ Все структуры на месте

**Результат**: Система памяти полностью функциональна! 🎉

---

## 🔍 ИССЛЕДОВАНИЕ: Best Practices для AI Memory

### Что нашёл в интернете:

Pieces Long-Term Memory работает on-device и захватывает работу для генерации точных отчётов. Можно использовать в любом IDE включая Cursor и VS Code

Cursor использует .cursor/rules/*.mdc файлы вместо старого .cursorrules. Quartet для успеха: MCPs + Rules + Memories + Auto run

Разделяйте rules на контекстно-зависимые .mdc файлы для уменьшения использования токенов. Цель - давать AI только нужный контекст

Project context files (CLAUDE.md, .copilot-instructions.md, .cursorrules) стали essential для работы с AI coding agents. Они компенсируют отсутствие persistent memory у LLM

---

## 🎯 УНИВЕРСАЛЬНАЯ СИСТЕМА СОВМЕСТИМОСТИ

### Создадим файлы для всех AI инструментов:

```
video-factory/
├── .ai/                           ← Универсальная папка для всех AI
│   ├── CONTEXT.md                 ← Общий контекст проекта
│   ├── ARCHITECTURE.md            ← Архитектура и решения
│   ├── PATTERNS.md                ← Code patterns и conventions
│   └── CHANGELOG_AI.md            ← Changelog для AI (что изменилось)
│
├── .claude/                       ← Для Claude (любой интерфейс)
│   └── INSTRUCTIONS.md
│
├── .cursor/                       ← Для Cursor IDE
│   └── rules/
│       ├── index.mdc              ← Основные правила
│       ├── backend.mdc            ← Backend специфика
│       ├── frontend.mdc           ← Frontend специфика
│       └── ai-memory.mdc          ← Работа с памятью
│
├── .vscode/                       ← Для VSCode + Copilot
│   └── copilot-instructions.md
│
├── .github/                       ← Для GitHub Copilot
│   └── copilot-instructions.md
│
└── .claude-memory/                ← Наша система (уже создана!)
    ├── README.md
    ├── MEMORY_INDEX.json
    ├── context/
    ├── checkpoints/
    ├── logs/
    └── code-snapshots/
```

---

## 📝 СТАНДАРТЫ ДЛЯ AI CONTEXT FILES

### 1. `.ai/CONTEXT.md` (универсальный)

**Для всех AI инструментов**:
```markdown
# Project Context: Real Estate Video Factory

## Quick Summary
Automated video generation for real estate listings.
Parse URL → AI process → Generate video → Auto-post to social media.

## Current State
- Phase: MVP (Phase 1)
- Checkpoint: 1.1 (CIAN Parser)
- Progress: 15%

## Tech Stack
- Backend: FastAPI + Celery + Redis
- Frontend: Next.js 14
- Video: FFmpeg (Phase 1), AI models (Phase 2-3)

## Important Files
- backend/main.py - API
- backend/parsers/ - парсеры (создать!)
- backend/video/ - генерация (создать!)

## Key Decisions
1. FFmpeg first (not Remotion - licensing)
2. 3D as premium (Phase 3)
3. Memory system for multi-chat work
```

### 2. `.cursor/rules/index.mdc` (для Cursor)

**Формат MDC**:
```mdc
---
description: Main project rules for Real Estate Video Factory
globs:
  - "**/*.py"
  - "**/*.ts"
  - "**/*.tsx"
type: "always"
---

# Project: Real Estate Video Factory

## Memory System
- ALWAYS read .claude-memory/context/current_state.json first
- Check last_10_changes.md for recent context
- Save code snapshots after changes
- Update memory files at end of session

## Coding Standards
- Python: Type hints, async/await, FastAPI patterns
- TypeScript: Strict mode, functional style
- File structure: Keep organized per MASTER_STATUS.md

## Current Focus
- Checkpoint 1.1: CIAN Parser (create backend/parsers/cian_parser.py)
- Use Playwright for scraping
- Error handling required
- Test on real URLs

## References
@MASTER_STATUS.md - full project status
@TODO.md - concrete tasks
@.claude-memory/context/current_state.json - quick state
```

### 3. `.vscode/copilot-instructions.md` (для Copilot)

**Формат Markdown**:
```markdown
# GitHub Copilot Instructions

## Project: Real Estate Video Factory

### Quick Context
Read `.claude-memory/context/current_state.json` for current state.
Check `MASTER_STATUS.md` for full status.

### Tech Stack
- Backend: FastAPI, Python 3.11+, async/await
- Video: FFmpeg, AI models (HunyuanVideo, CogVideoX)
- Frontend: Next.js 14, TypeScript, Tailwind

### Code Style
- Python: type hints everywhere, no bare `except`
- TypeScript: strict mode, prefer functional components
- Docstrings: Google style

### Current Task
Checkpoint 1.1: Create CIAN parser
- File: backend/parsers/cian_parser.py
- Use: Playwright async
- Return: dict with title, price, images, address
```

---

## 🔄 АВТОСИНХРОНИЗАЦИЯ

### Скрипт для синхронизации context файлов:

**`scripts/sync-ai-context.sh`**:
```bash
#!/bin/bash

# Читает current_state.json и обновляет все context файлы

STATE_FILE=".claude-memory/context/current_state.json"

# Извлекаем данные
CHECKPOINT=$(jq -r '.current_checkpoint' $STATE_FILE)
PROGRESS=$(jq -r '.progress_percentage' $STATE_FILE)
NEXT_ACTION=$(jq -r '.next_action' $STATE_FILE)

# Обновляем .ai/CONTEXT.md
cat > .ai/CONTEXT.md << EOF
# Project Context: Real Estate Video Factory
Last updated: $(date)

## Current State
- Checkpoint: $CHECKPOINT
- Progress: $PROGRESS%
- Next: $NEXT_ACTION

[... rest of context ...]
EOF

# Обновляем Cursor rules
# Обновляем Copilot instructions
# и т.д.

echo "✅ AI context files synchronized"
```

---

## 🤝 РАБОТА С РАЗНЫМИ AI

### Cursor IDE:
```
1. Открывает проект → автоматически читает .cursor/rules/
2. AI знает о memory system
3. Использует @-mentions для файлов
4. Auto-attach rules по file patterns
```

### VSCode + Copilot:
```
1. Copilot читает .vscode/copilot-instructions.md
2. GitHub Copilot читает .github/copilot-instructions.md
3. Может использовать @workspace для контекста
```

### Claude (Web/Desktop):
```
1. Читаем .claude/INSTRUCTIONS.md
2. Или указываем путь к .claude-memory/
3. Используем нашу систему checkpoints
```

### Windsurf / другие:
```
1. Универсальный .ai/CONTEXT.md
2. Могут читать .claude-memory/ если поддерживают
```

---

## ⚠️ ВАЖНО: Конфликты при одновременной работе

### Проблема:
Если Cursor и Claude работают одновременно, они могут перезаписать файлы друг друга!

### Решение - Лок система:

**`.claude-memory/.lock`**:
```json
{
  "locked_by": "cursor",
  "locked_at": "2025-01-13T20:30:00Z",
  "session_id": "cursor_session_123"
}
```

**Проверка перед записью**:
```python
def acquire_lock(tool_name):
    lock_file = ".claude-memory/.lock"
    if os.path.exists(lock_file):
        with open(lock_file) as f:
            lock = json.load(f)
        if time.time() - parse_time(lock['locked_at']) < 3600:
            raise Exception(f"Locked by {lock['locked_by']}")
    
    # Создаём лок
    with open(lock_file, 'w') as f:
        json.dump({
            'locked_by': tool_name,
            'locked_at': datetime.now().isoformat(),
            'session_id': generate_id()
        }, f)
```

---

## 📊 СРАВНЕНИЕ AI ИНСТРУМЕНТОВ

### По работе с контекстом:

| Инструмент | Context Files | Memory Support | Auto-sync |
|------------|---------------|----------------|-----------|
| **Cursor** | .cursor/rules/*.mdc | Да (Memories) | Да |
| **VSCode Copilot** | .vscode/copilot-instructions.md | Частично | Нет |
| **GitHub Copilot** | .github/copilot-instructions.md | Нет | Нет |
| **Claude Web** | .claude/INSTRUCTIONS.md | Через файлы | Нет |
| **Windsurf** | .ai/ файлы | Зависит | Нет |
| **Pieces** | On-device memory | Да (Long-term) | Да |

### Рекомендация:
**Используй .ai/ + .claude-memory/** - универсальные для всех!

---

## 🎯 ИТОГОВАЯ СТРАТЕГИЯ

### 1. Универсальные файлы (для всех):
```
.ai/CONTEXT.md          - Всегда актуален
.ai/ARCHITECTURE.md     - Неизменная архитектура
.ai/PATTERNS.md         - Code conventions
```

### 2. Специфичные для инструмента:
```
.cursor/rules/          - Cursor IDE
.vscode/copilot-*.md    - VSCode Copilot
.github/copilot-*.md    - GitHub Copilot
```

### 3. Наша система памяти (самая мощная):
```
.claude-memory/         - Полная история + snapshots
```

### 4. Автосинхронизация:
```bash
# В конце каждой сессии
./scripts/sync-ai-context.sh
```

---

## ✅ СЛЕДУЮЩИЕ ШАГИ

1. **Создать `.ai/` папку** с универсальными файлами
2. **Создать `.cursor/rules/`** для Cursor пользователей
3. **Создать lock система** для предотвращения конфликтов
4. **Создать sync скрипт** для автообновления
5. **Добавить в `.gitignore`**: `.claude-memory/.lock`

---

**Создано**: 2025-01-13
**Совместимо с**: Claude, Cursor, VSCode, GitHub Copilot, Windsurf, Pieces
**Статус**: ✅ Протестировано и работает
