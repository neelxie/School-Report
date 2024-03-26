# Use the official Python image as a base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file separately to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole directory contents into the container at /app
COPY . /app

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variables
ENV TIMEOUT=90
ENV WORKERS=3
ENV THREADS=3

# Run gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "manage:app", "--timeout", "90", "--workers=3", "--threads=3", "--worker-class=gevent"]
