# Base image  
FROM python:3.14-rc-slim-bookworm

# Working directory inside the container
WORKDIR /app
 
COPY app.py /app/

# Install system dependencies (for OpenCV and other libraries)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libsm6 libxrender1 libxext6 libopencv-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
 
EXPOSE 8501
 
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
