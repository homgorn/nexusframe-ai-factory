# 🎬 Project Context: Real Estate Video Factory

> **Last Updated**: 2025-01-13  
> **For**: All AI assistants (Claude, Cursor, Copilot, Windsurf, etc.)

---

## ⚡ Quick Summary (10 seconds read)

**What**: Automated SaaS for creating real estate video ads  
**Input**: CIAN/Avito URL or manual photos  
**Output**: Professional video + auto-post to YouTube/TikTok/Instagram  
**Stage**: MVP Development (Phase 1 of 6)  
**Progress**: 15%

---

## 🎯 Current State

### RIGHT NOW:
- **Phase**: 1 - MVP (FFmpeg Pipeline)
- **Checkpoint**: 1.1 - CIAN Parser
- **Status**: Not started
- **Next Action**: Create `backend/parsers/cian_parser.py`
- **Blocker**: None
- **ETA to MVP**: 3-5 days of work

### Last Session:
- Date: 2025-01-13
- Duration: 7 hours
- Tokens: 139,000
- Achievement: Created project structure + memory system

---

## 🏗️ Architecture

### Stack (Confirmed):
```
Frontend:  Next.js 14 + TypeScript + TailwindCSS
Backend:   FastAPI + Python 3.11+
Queue:     Celery + Redis
Database:  PostgreSQL + SQLAlchemy
Storage:   MinIO (S3-compatible)
Video:     FFmpeg (Phase 1) → AI models (Phase 2-3)
Deploy:    Docker Compose
```

### Phases:
1. **MVP** (Current): FFmpeg pipeline - simple slideshow
2. **AI**: Text/Image/Audio AI enhancement
3. **3D**: Hunyuan3D + Gaussian Splatting + Unreal Engine
4. **Advanced**: Multiple parsers, templates
5. **Social**: Auto-post to all platforms with SEO
6. **Production**: Scale, auth, billing

---

## 📁 Key Files & Folders

### MUST READ FIRST:
```
MASTER_STATUS.md                 - Full project status (read this!)
TODO.md                          - Concrete tasks with checklists
.claude-memory/context/          - Quick context (2KB, instant load)
  ├── current_state.json         - Current checkpoint, progress
  └── last_10_changes.md         - Recent changes (last 10)
```

### Code Structure:
```
backend/
  ├── main.py                    ✅ API structure (needs logic!)
  ├── parsers/                   ❌ NOT CREATED (need this!)
  │   └── cian_parser.py         ← CHECKPOINT 1.1
  ├── video/                     ❌ NOT CREATED
  │   └── ffmpeg_generator.py    ← CHECKPOINT 1.2
  └── tasks.py                   ❌ NOT CREATED (Celery)

frontend/                        ❌ EMPTY FOLDER
.claude-memory/                  ✅ Memory system working!
```

---

## 🎓 Important Context

### Why this exists:
Real estate agents need professional videos but:
- Hiring videographers is expensive ($500+ per video)
- Manual editing takes hours
- Need videos in multiple formats (YT, IG, TikTok)

### Our solution:
1. Parse listing URL → extract photos/text
2. AI enhances quality + generates SEO copy
3. Auto-generate video in all formats
4. One-click post to all social media
5. **Total time**: 2-3 minutes vs 3+ hours manual

### Unique selling point:
- **Phase 3**: 3D virtual tours from 2D photos (no other service has this!)
- **Phase 5**: Full automation (parse → generate → post)

---

## 💻 Coding Standards

### Python (Backend):
```python
# ✅ GOOD
async def parse_cian(url: str) -> dict:
    """Parse CIAN listing.
    
    Args:
        url: CIAN listing URL
        
    Returns:
        dict with title, price, images, address
        
    Raises:
        ValueError: Invalid URL
    """
    async with async_playwright() as p:
        ...

# ❌ BAD
def parse(url):  # No type hints!
    try:
        ...
    except:  # Bare except!
        pass  # Silent failure!
```

**Rules**:
- Type hints EVERYWHERE
- async/await for I/O
- Google-style docstrings
- No bare `except`
- FastAPI patterns

### TypeScript (Frontend):
```typescript
// ✅ GOOD
interface VideoConfig {
  aspectRatio: '16:9' | '9:16' | '1:1';
  duration: number;
}

const generateVideo = async (config: VideoConfig): Promise<string> => {
  ...
}

// ❌ BAD
const generateVideo = (config: any) => {  // any!
  ...
}
```

**Rules**:
- Strict mode
- Functional components (React)
- No `any` types
- TailwindCSS for styling

---

## 🔍 How to Work With This Project

### For new AI session:

**Step 1**: Load quick context (fast!)
```
Read: .claude-memory/context/current_state.json
Read: .claude-memory/context/last_10_changes.md
```
**Time**: 5-10 seconds, ~2KB data

**Step 2**: Understand current task
```
Read: TODO.md → section "Checkpoint 1.1"
```

**Step 3**: Start working!
```
Current task: Create CIAN parser
File: backend/parsers/cian_parser.py
Tech: Playwright (async)
```

**Step 4**: After work, update memory
```
Update: .claude-memory/context/current_state.json
Create: .claude-memory/logs/YYYY-MM-DD_session_N.md
Update: .claude-memory/context/last_10_changes.md
```

---

## 🐛 Known Issues

### Critical (blocks MVP):
1. **Parsers are stubs** - only return mock data
2. **FFmpeg not implemented** - only asyncio.sleep()
3. **Celery tasks file missing** - needs creation
4. **Frontend empty** - zero code

### Non-critical:
1. Docker not tested locally
2. Database models not created
3. MinIO bucket not auto-created

---

## 💡 Key Decisions Made

| Date | Decision | Reason |
|------|----------|--------|
| 2025-01-13 | FFmpeg first (not Remotion) | Faster MVP, no licensing |
| 2025-01-13 | 3D as Phase 3 premium | Differentiation |
| 2025-01-13 | Memory system for multi-chat | Token efficiency |
| 2025-01-13 | Social media in Phase 5 | Complete automation |

---

## 📚 External Resources

### APIs we'll use:
- **YouTube Data API v3** - video upload
- **TikTok Content Posting API v2** - auto-post
- **Meta Graph API** - Instagram/Facebook
- **Claude/GPT API** - text generation
- **ElevenLabs** - voice generation
- **Mubert** - music generation

### AI Models (Phase 2-3):
- **HunyuanVideo** - free (Colab/Kaggle)
- **CogVideoX** - free (Colab/Kaggle)
- **Kling** - paid ($6.99/month)
- **Runway Gen-4** - paid ($95/month)
- **Hunyuan3D** - free (Phase 3)

---

## 🎯 Success Metrics

### MVP Ready When:
- [x] Can parse CIAN URL
- [x] Extract photos/text
- [x] Generate 30s video with FFmpeg
- [x] Download video works
- [x] Takes < 3 minutes end-to-end

### Business Metrics:
- **Cost per video**: < $0.50
- **Generation time**: < 3 min
- **Success rate**: > 95%
- **User satisfaction**: > 4.5/5

---

## 🚀 Quick Commands

### For Claude/AI assistants:

**Check status**:
```
What's the current checkpoint and progress?
→ Read current_state.json
```

**Start work**:
```
Let's work on Checkpoint 1.1 - CIAN Parser
→ Read TODO.md, create cian_parser.py
```

**Get code from checkpoint**:
```
Show me the code from checkpoint 1.1
→ Read .claude-memory/checkpoints/checkpoint_1.1_DONE.md
```

**Update memory**:
```
Update memory with today's work
→ Update current_state.json, create session log
```

---

## 🔗 Links

- **Full Status**: MASTER_STATUS.md
- **Tasks**: TODO.md
- **Roadmap**: ROADMAP.md (artifact, need to save)
- **Memory System**: .claude-memory/README.md
- **Quick Start**: QUICK_START_FOR_NEW_CHAT.md

---

## 🎬 Let's Build!

**Current Priority**: Checkpoint 1.1 - CIAN Parser

**What to do**: Create `backend/parsers/cian_parser.py` with Playwright

**Estimated time**: 2-4 hours

**Tokens budget**: ~15,000

---

**Remember**: This is a living document. Update it when architecture or key decisions change!
