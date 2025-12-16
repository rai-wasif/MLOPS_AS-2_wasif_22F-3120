# Use a minimal Python image as the base for the training environment
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project code into the container
COPY . .

# Command to run when the container starts: executes the training script (Task 3.1)
CMD ["python", "src/train.py"]