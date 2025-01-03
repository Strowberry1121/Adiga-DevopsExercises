# Use Python base image
FROM python:3.9

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Create a directory for SQLite data
RUN mkdir -p /app/db

# Expose the application port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]