FROM python:3.10-slim

# Create a working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories before copying files
RUN mkdir -p ./templates ./static/uploads ./static/key

# Copy application files
COPY app.py .
COPY templates/ ./templates/

# Note: We don't copy the static directory since we created it manually
# This avoids the "static directory not found" error

# Install required Python modules
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set environment variables
ENV PORT=5000
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]