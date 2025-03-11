# Use an official Python image as the base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE $PORT

# Command to run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]

RUN mkdir -p /app/static/uploads && chmod -R 777 /app/static/uploads