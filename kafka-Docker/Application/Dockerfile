# Dockerfile
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install Python libraries
RUN pip install confluent-kafka

# Copy the Python script into the container
COPY app.py .

# Command to run when the container starts
CMD ["python", "app.py"]
