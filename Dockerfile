# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Prevent interactive prompts during apt package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and basic system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Bypass strict corporate SSL/TLS proxy inspections
ENV PIP_TRUSTED_HOST="pypi.org pypi.python.org files.pythonhosted.org github.com objects.githubusercontent.com raw.githubusercontent.com"
ENV PYTHONHTTPSVERIFY=0

# Install Python dependencies directly
RUN pip3 install --no-cache-dir \
    Flask \
    Flask-SQLAlchemy \
    pymysql \
    Flask-Migrate \
    python-dotenv \
    spacy

# Download spaCy small language model (Fastest, low memory footprint, good for development)
RUN python3 -m spacy download es_core_news_sm

# Copy the rest of the API code to the container
COPY . .

# Expose the default Flask port
EXPOSE 5000

# Command to start the application
CMD ["python3", "run.py"]
