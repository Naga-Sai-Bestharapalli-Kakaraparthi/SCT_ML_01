# 1. Base image with Python
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy project files into the container
COPY . /app

# 5. Run the main ETL script directly
CMD ["python", "main.py"]
