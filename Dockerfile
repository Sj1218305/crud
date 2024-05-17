
# Use the official Python image from the Docker Hub
FROM python:slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the devices.json file exists
RUN touch devices.json

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]
