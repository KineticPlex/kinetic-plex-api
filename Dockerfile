# Use official Python slim image (Debian-based, highly optimized and lightweight)
FROM python:3.10-slim

# Prevent Python from writing .pyc files to disk and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Bypass strict corporate SSL/TLS proxy inspections
ENV PIP_TRUSTED_HOST="pypi.org pypi.python.org files.pythonhosted.org github.com objects.githubusercontent.com raw.githubusercontent.com"
ENV PYTHONHTTPSVERIFY=0

# Install Python dependencies directly (wheels will download and install in seconds)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    Flask \
    Flask-SQLAlchemy \
    pymysql \
    Flask-Migrate \
    python-dotenv \
    spacy

# Download spaCy small language model (Fastest, low memory footprint, good for development)
RUN python -m spacy download es_core_news_sm

# Copy the rest of the API code to the container
COPY . .

# Expose the custom Flask port
EXPOSE 9001

# Command to start the application
CMD ["python", "run.py"]