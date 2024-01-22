# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and activate it
RUN python3 -m venv env
RUN /bin/bash -c "source env/bin/activate"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7755 available to the world outside this container
EXPOSE 7755

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["bash", "run.sh"]
