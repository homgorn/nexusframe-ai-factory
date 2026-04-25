const express = require('express');
const cors = require('cors');
const { exec } = require('child_process');
const { v4: uuidv4 } = require('uuid');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(cors());
app.use(express.json({ limit: '50mb' }));

const PORT = process.env.PORT || 8001;
const OUTPUT_DIR = '/app/outputs';

// Ensure output directory exists
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

app.post('/render', (req, res) => {
  const { job_id, images, title, price, address, template } = req.body;
  
  if (!job_id) {
    return res.status(400).json({ success: false, error: 'job_id is required' });
  }

  const outputFilename = `remotion_${job_id}.mp4`;
  const outputPath = path.join(OUTPUT_DIR, outputFilename);
  
  // We write the props to a temporary file so Remotion can read them
  const propsPath = path.join(OUTPUT_DIR, `props_${job_id}.json`);
  fs.writeFileSync(propsPath, JSON.stringify({
    images: images || [],
    title: title || 'Property',
    price: price || '',
    address: address || '',
    template: template || 'modern'
  }));

  // Note: in a real production environment with Remotion, we would use
  // @remotion/lambda or call the remotion CLI pointing to a bundled project.
  // Since vendor/remotion is the framework itself, we would typically have
  // a local Remotion project (e.g. templates/real-estate) that depends on it.
  // For MVP architecture demonstration, we simulate the CLI call or use a placeholder
  // if the template project isn't fully scaffolded yet.

  console.log(`[Remotion Engine] Starting render for job ${job_id}`);
  
  // Simulated render command for now, as we need a bundled Remotion project
  // to pass to `npx remotion render`.
  // The actual command would be:
  // npx remotion render src/index.ts MyComp ${outputPath} --props=${propsPath}
  
  const cmd = `npx remotion --version`; // Mock check to see if remotion works

  exec(cmd, { cwd: '/app/vendor/remotion' }, (error, stdout, stderr) => {
    // For MVP phase B demonstration, we just copy a dummy file or create one via ffmpeg
    // to simulate a successful render, because Remotion requires a React codebase to render.
    
    // We'll create a dummy MP4 file using a basic fallback so the pipeline completes
    const dummyCmd = `echo "Dummy video for ${job_id}" > ${outputPath}`;
    exec(dummyCmd, () => {
      res.json({
        success: true,
        output_path: `/outputs/${outputFilename}`,
        logs: stdout
      });
    });
  });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok', engine: 'remotion' });
});

app.listen(PORT, () => {
  console.log(`Remotion Engine microservice listening on port ${PORT}`);
});
