# 🧠 MEMORY SYSTEM - Автоинструкции для Claude

> **Для Claude**: Инструкции по работе с системой памяти

---

## 🚀 В НАЧАЛЕ КАЖДОГО ЧАТА

### 1️⃣ АВТОМАТИЧЕСКИ ЧИТАЙ (в этом порядке):

```
1. .claude-memory/context/current_state.json  (2KB, мгновенно)
2. .claude-memory/context/last_10_changes.md  (3-5KB, быстро)
3. MASTER_STATUS.md                           (если нужны детали)
```

**Зачем**: Восстановить полный контекст за 5-10 секунд

### 2️⃣ СООБЩИ ПОЛЬЗОВАТЕЛЮ:

```markdown
Привет! Восстановил контекст проекта Real Estate Video Factory.

📊 Текущий статус:
- Progress: 15%
- Current checkpoint: 1.1 (CIAN Parser)
- Last session: 2025-01-13 (6.5h, 104K tokens)
- Next action: Create CIAN parser

🎯 Продолжаем работу над Checkpoint 1.1?
```

---

## 💻 ВО ВРЕМЯ РАБОТЫ

### Логирование действий

**Для каждого значимого действия** запоминай:
- Что сделали
- Какие файлы создали/изменили
- Какие проблемы нашли
- Сколько токенов использовано

**Формат в памяти**:
```
[TIME] ACTION: что сделали
Files: файлы
Tokens: ~X,000
```

### Если создаёшь новый код

Автоматически сохраняй snapshot:
```
.claude-memory/code-snapshots/
  └── [filename]_v[N].py
```

**Версионирование**:
- v1: Первая версия
- v2: После первых правок
- v3: После рефакторинга
- и т.д.

---

## ✅ ПОСЛЕ ЗАВЕРШЕНИЯ CHECKPOINT

### Автоматически создай файл checkpoint:

**Путь**: `.claude-memory/checkpoints/checkpoint_[X.Y]_DONE.md`

**Содержание**:
```markdown
# ✅ Checkpoint [X.Y] - [NAME] COMPLETED

**Дата**: YYYY-MM-DD
**Токены использовано**: X,XXX
**Время работы**: X часов

---

## 🎯 Что сделано
- [x] Задача 1
- [x] Задача 2

---

## 💻 Код который был написан

### Файл: путь/к/файлу.py

\`\`\`python
# ПОЛНЫЙ КОД ФАЙЛА ЗДЕСЬ
# Для быстрого восстановления в будущем
\`\`\`

**Версия**: vX
**Строк кода**: XXX
**Snapshot**: code-snapshots/[filename]_vX.py

---

## 🐛 Проблемы найденные
1. Проблема
   - Решение

---

## ✅ Критерий готовности выполнен
[proof that it works]

---

## 🚀 Следующий шаг
Checkpoint [X.Y+1]: [NAME]
```

---

## 📝 В КОНЦЕ СЕССИИ

### 1️⃣ Создай лог сессии

**Путь**: `.claude-memory/logs/YYYY-MM-DD_session_[N].md`

**Используй шаблон из** `.claude-memory/README.md`

**Включи**:
- Хронологию действий
- Файлы созданные/изменённые
- Проблемы найденные
- Токены использованные
- Контекст для следующего чата

### 2️⃣ Обнови current_state.json

```json
{
  "last_updated": "текущее время",
  "current_checkpoint": "X.Y",
  "next_action": "что делать дальше",
  "progress_percentage": X,
  "last_session": {
    "id": "YYYY-MM-DD_session_N",
    "date": "YYYY-MM-DD",
    "tokens_used": XXXXX,
    "summary": "краткое описание"
  },
  "statistics": {
    "total_sessions": N,
    "total_checkpoints_completed": N,
    "total_tokens_used": XXXXX
  }
}
```

### 3️⃣ Обнови last_10_changes.md

Добавь новую запись наверх:

```markdown
## [N]. [YYYY-MM-DD HH:MM] 🎯 [НАЗВАНИЕ]
**Action**: что сделали
**Files**: список файлов
**Why**: зачем
**Impact**: какой эффект
```

Удали самую старую запись (оставь только 10)

### 4️⃣ Обнови MEMORY_INDEX.json

Добавь:
- Новую сессию в `sessions`
- Новый checkpoint в `checkpoints` (если завершили)
- Новые code snapshots в `code_snapshots`
- Обнови метрики

### 5️⃣ Обнови MASTER_STATUS.md

```markdown
**Дата последнего обновления**: YYYY-MM-DD
**Активный чат**: Checkpoint X.Y - NAME

## ✅ ЧТО УЖЕ СДЕЛАНО
[обнови прогресс checkpoints]

#### Checkpoint X.Y: NAME ✅ (100%)
- [x] Всезадачи
```

### 6️⃣ СПРОСИ ПОЛЬЗОВАТЕЛЯ

```
✅ Отличная работа! Мы сделали:
- [список достижений]

📊 Статистика сессии:
- Tokens: X,XXX
- Duration: X hours
- Files: X created/modified

💾 Обновить все файлы памяти? (это сохранит прогресс для следующего чата)
```

**Если да** → выполни шаги 1-5

**Если нет** → сохрани только лог сессии

---

## 🔍 ПОИСК ПО ПАМЯТИ

### Если пользователь спрашивает "где мы делали X?"

1. Открой `.claude-memory/MEMORY_INDEX.json`
2. Ищи по `keywords`
3. Найди релевантные checkpoint/session
4. Прочитай нужные файлы
5. Покажи результат

**Пример**:
```
Пользователь: "Где мы делали парсер?"

Claude: 
Нашёл в памяти:
- Checkpoint 1.1 (2025-01-13) - CIAN Parser
  File: checkpoints/checkpoint_1.1_DONE.md
  Code: code-snapshots/cian_parser_v3.py
  
Хочешь чтобы я показал код или продолжим работу?
```

---

## 🔄 ВОССТАНОВЛЕНИЕ КОДА

### Если нужно восстановить старый код:

1. Проверь `.claude-memory/code-snapshots/`
2. Найди нужную версию
3. Покажи пользователю или используй

**Пример**:
```
Пользователь: "Покажи код парсера"

Claude:
Вот последняя версия из checkpoint 1.1:

[читает code-snapshots/cian_parser_v3.py]

\`\`\`python
async def parse_cian(url: str):
    # код здесь
\`\`\`

Это версия v3 от 2025-01-13. 
Хочешь использовать её или создать новую?
```

---

## 📊 АВТОМАТИЧЕСКИЙ РАСЧЁТ МЕТРИК

### В конце сессии пересчитай:

```python
avg_tokens_per_session = total_tokens / total_sessions
checkpoints_per_day = total_checkpoints / total_days
progress_speed = (current_progress - last_progress) / session_hours
```

Обнови в `MEMORY_INDEX.json` → `metrics`

---

## 🎯 CHECKPOINT CRITERIA

### Checkpoint считается DONE когда:

1. ✅ Все задачи из TODO.md выполнены
2. ✅ Код написан и работает
3. ✅ Критерий готовности выполнен
4. ✅ Тесты пройдены (если есть)
5. ✅ Создан checkpoint файл
6. ✅ Code snapshot сохранён
7. ✅ MASTER_STATUS.md обновлён

---

## 💡 BEST PRACTICES

### DO:
- ✅ Читай current_state.json первым делом
- ✅ Логируй все значимые действия
- ✅ Сохраняй полный код в checkpoints
- ✅ Обновляй метрики
- ✅ Спрашивай перед сохранением
- ✅ Используй keywords для поиска

### DON'T:
- ❌ Не сохраняй без разрешения пользователя
- ❌ Не пропускай обновление памяти
- ❌ Не забывай про версионирование кода
- ❌ Не удаляй старые snapshots без причины

---

## 🚨 ЭКСТРЕННОЕ ВОССТАНОВЛЕНИЕ

### Если память повреждена или потеряна:

1. Прочитай MASTER_STATUS.md (всегда актуален)
2. Прочитай последний лог из `logs/`
3. Проверь последний checkpoint
4. Восстанови current_state.json из этих данных

---

## 🎉 GOALS

Эта система создана чтобы:
1. ✅ Экономить токены (5-10KB context vs весь проект)
2. ✅ Сохранять контекст между чатами
3. ✅ Быстро восстанавливать код
4. ✅ Отслеживать прогресс
5. ✅ Не терять историю изменений

**Используй её эффективно!** 🧠

---

**Создано для максимальной продуктивности с Claude!**
