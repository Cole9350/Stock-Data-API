# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5001

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
