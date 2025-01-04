# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5050

# Command to run the app
CMD ["python", "app.py"]