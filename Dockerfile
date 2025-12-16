# Use an official Python runtime as a parent image, minimal size
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency file and install dependencies
# This is key for efficient Docker caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the models and the API code into the container
# Ensure these folders (api and models) exist in your project root
COPY api /app/api
COPY models /app/models

# Expose the port the app runs on (FastAPI/Uvicorn default)
EXPOSE 8000

# Command to run the application using Uvicorn
# This starts the FastAPI server inside the container
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]