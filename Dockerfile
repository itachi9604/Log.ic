# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 outside the container
EXPOSE 80

# Set an environment variable for the volume path
ENV LOG_VOLUME_PATH /app/logs/log_file.log

# Start the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:80", "wsgi:app"]