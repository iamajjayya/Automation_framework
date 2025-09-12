# Use lightweight Python base image
FROM python:3.11-slim

# Install dependencies for Chromium & Selenium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    chromium \
    chromium-driver \
    fonts-liberation \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libxrandr2 \
    libpangocairo-1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables so Python & Chrome know where Chromium is
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_PATH=/usr/bin/chromium

# Set working directory inside container
WORKDIR /app

# Copy only requirements.txt first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your project
COPY . .

# Add and make run script executable
COPY run.sh .
RUN chmod +x run.sh

# Default command to run when container starts
CMD ["./run.sh"]
