# Base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /usr/src/backend

# Copy and install dependencies
COPY requirements.txt . 
RUN pip install -r requirements.txt

# Copy project files into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
