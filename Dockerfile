# Use Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the application code (including app.py)
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000  

# Start the Flask application
CMD ["python", "app.py"]

