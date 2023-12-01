
# Use the lightest Python image
FROM python:alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY scraper.py .

# Run the Python script
CMD ["python", "scraper.py"]
