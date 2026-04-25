const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');
const { v4: uuidv4 } = require('uuid');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json({ limit: '50mb' }));

const PORT = process.env.PORT || 8003;
const OUTPUT_DIR = '/app/outputs';

if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

app.post('/render', (req, res) => {
  const { job_id, images, title, price, address } = req.body;
  
  if (!job_id) {
    return res.status(400).json({ success: false, error: 'job_id is required' });
  }

  const outputFilename = `hyperframes_${job_id}.mp4`;
  const outputPath = path.join(OUTPUT_DIR, outputFilename);
  
  console.log(`[HyperFrames Engine] Starting render for job ${job_id}`);
  
  // Simulated hyperframes render process.
  // In a real scenario, we would run `npx hyperframes render` or `bun run render`
  // pointing to the generated HTML composition.
  
  // Create a dummy output to simulate successful rendering
  const dummyCmd = `echo "Dummy HyperFrames HTML video for ${job_id}" > ${outputPath}`;
  exec(dummyCmd, (error, stdout, stderr) => {
    res.json({
      success: true,
      output_path: `/outputs/${outputFilename}`,
      engine: 'hyperframes'
    });
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok', engine: 'hyperframes' });
});

app.listen(PORT, () => {
  console.log(`HyperFrames Engine microservice listening on port ${PORT}`);
});
