FROM python:3.10-slim

# Create a working directory
WORKDIR /app

# Copy necessary files
COPY ransomware.py .
COPY entrypoint.sh .
COPY target_files ./target_files

# Install required Python modules
RUN pip install cryptography

# Make entrypoint executable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
