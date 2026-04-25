FROM node:20-slim

WORKDIR /app/engine

# Copy package files
COPY package*.json ./
RUN npm install

# Copy server code
COPY server.js ./

EXPOSE 8002

CMD ["npm", "start"]
