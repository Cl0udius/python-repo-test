# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the startup script into the container
COPY start.sh /app/start.sh

# Ensure the startup script is executable
RUN chmod +x /app/start.sh

# Create Plato folder
RUN mkdir /python

# Copy python lib
COPY plato.py /python

# Command to run the startup script
CMD ["/bin/sh", "/app/start.sh"]
