<<<<<<< HEAD
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

=======
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME Wisecow

CMD ["python", "app.py"]
>>>>>>> 936fe8e5e27acbc4b9b06de2134b3d402bd6328f
