FROM ubuntu AS test

# Set the working directory in the image
WORKDIR /app

# Install the necesssary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set environment variables
ENV NAME world

# Copy the files from the host file system to the image file system
COPY . /app

FROM gcr.io/distroless/python3 AS diployer

# Copy the compiled binary from the build stage
COPY --from=test /app /app

# Set the entrypoint for the container to run the binary
ENTRYPOINT ["python3"]
