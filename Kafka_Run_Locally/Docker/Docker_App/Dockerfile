FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code
COPY . /app

# Command to run the app
CMD ["python", "app.py"]
