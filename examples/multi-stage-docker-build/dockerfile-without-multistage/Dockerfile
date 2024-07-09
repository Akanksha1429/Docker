FROM ubuntu as test

# Set the working directory in the image
WORKDIR /app

# Copy the files from the host file system to the image file system
COPY . /app

# Install the necesssary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set environment variables
ENV NAME world

# Run a command to start the application
CMD ["python3", "calculator.py"] 
