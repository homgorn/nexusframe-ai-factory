FROM node:20-slim

# Install necessary libraries for Chromium and rendering
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/engine

# Copy package files
COPY package*.json ./
RUN npm install

# Copy server code
COPY server.js ./

EXPOSE 8001

CMD ["npm", "start"]
