FROM python:3.10-slim

# Create a working directory
WORKDIR /app

# Copy application files
COPY app.py .
COPY requirements.txt .
COPY templates ./templates
COPY static ./static

# Create necessary directories
RUN mkdir -p ./static/uploads ./static/key

# Install required Python modules
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Set environment variables
ENV PORT=5000
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]