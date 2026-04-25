const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 8002;

app.post('/orchestrate', (req, res) => {
  const { job_id, parsed_data } = req.body;
  
  if (!job_id || !parsed_data) {
    return res.status(400).json({ error: 'job_id and parsed_data are required' });
  }

  console.log(`[Open-Harness] Orchestrating job ${job_id}`);
  
  // In production, this would initialize an open-harness session
  // import { Harness } from '/app/vendor/open-harness/sdk';
  // const harness = new Harness({...});
  // harness.route(parsed_data);

  // MVP Mock routing logic:
  // Decides which video engine is best suited for the scraped data.
  let selectedEngine = 'ffmpeg'; // fallback
  let confidence = 0.5;
  let reason = "Fallback to default engine";

  const description = (parsed_data.title + " " + parsed_data.description).toLowerCase();

  // Keyword heuristic matching (simulating AI agent)
  if (description.includes("премиум") || description.includes("элитн") || description.includes("luxury")) {
    selectedEngine = 'remotion';
    confidence = 0.92;
    reason = "Premium keywords detected. Remotion provides highest quality animations.";
  } else if (description.includes("динамичн") || description.includes("быстро") || description.includes("reels") || description.includes("tiktok")) {
    selectedEngine = 'hyperframes';
    confidence = 0.88;
    reason = "Social media keywords detected. HyperFrames is optimized for fast, HTML-based social shorts.";
  } else if (description.includes("график") || description.includes("статистика") || description.includes("инвестиц")) {
    selectedEngine = 'manim';
    confidence = 0.85;
    reason = "Data/investment keywords detected. Manim CE generates clear infographics.";
  } else if (description.includes("3d") || description.includes("тур") || description.includes("виртуальн")) {
    selectedEngine = 'hy-world-3d';
    confidence = 0.75;
    reason = "3D Tour requested. Routing to Tencent HY-World engine (GPU required).";
  }

  res.json({
    success: true,
    routing: {
      engine: selectedEngine,
      confidence: confidence,
      reason: reason
    },
    orchestrated_at: new Date().toISOString()
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'open-harness-orchestrator' });
});

app.listen(PORT, () => {
  console.log(`Open-Harness Orchestrator listening on port ${PORT}`);
});
