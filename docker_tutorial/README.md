## Commands for running Dockerfile and Docker Container
```bash
# Build the Docker image
docker build -t app-image .

# List the Docker images
docker images

# Run the Docker container
docker run -itd --name app-container -p 5000:5000 --volume {$PWD}:/app app-image

# List the Docker containers
docker ps
docker ps -a

# Stop, start, and restart the Docker container
docker stop app-container
docker start app-container
docker restart app-container

# Execute the bash shell in the Docker container
docker exec -it app-container bash

# Stop and remove the Docker container and image
docker stop app-container
docker rm app-container
docker rmi app-image
```

## Commands for running Docker Compose
```bash
docker-compose up --build -d
```


## Commands for interact with Docker Hub
```bash
# Login to Docker Hub
docker login

# Commit the Docker container to a Docker image
docker commit flask-server thakorneyp11/flask-server:v0.1

# List the Docker images
docker images

# Push the Docker image to Docker Hub
docker push thakorneyp11/flask-server:v0.1

# Pull the Docker image from Docker Hub
docker pull thakorneyp11/flask-server:v0.1
```
