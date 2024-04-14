#!/bin/bash

USERNAME="mihayy9"
REPO_NAME="sistemska"
TAG="latest"

docker pull $USERNAME/$REPO_NAME:$TAG

docker run -d --name sistemska_container $USERNAME/$REPO_NAME:$TAG

echo "Container sistemska_container is running using image $USERNAME/$REPO_NAME:$TAG"