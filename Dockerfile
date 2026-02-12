# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY src/ ./src

# Expose port
EXPOSE 8080

# Run the app
CMD ["python", "src/app.py"]

