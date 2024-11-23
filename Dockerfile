FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential meson && \
    apt-get clean

# Copy the application code and requirements
COPY app.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the application
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]
