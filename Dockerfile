FROM python:3.12-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg imagemagick curl && \
    rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY backend/ ./backend/
COPY docs/ ./docs/
COPY sdk/ ./sdk/
COPY site/ ./site/
COPY frontend/ ./frontend/
COPY logo.svg .
COPY README.md .

# Work from backend
WORKDIR /app/backend

# Data directory
RUN mkdir -p /app/data

# Run as non-root
RUN useradd -m -r nordai && chown -R nordai:nordai /app
USER nordai

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["python", "main.py"]
