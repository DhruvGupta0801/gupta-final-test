# Use the official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port
EXPOSE 5000

# Run the app with Gunicorn, with logging, timeout, and workers
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--log-level", "debug", "--timeout", "120", "--workers", "2", "app:app"]