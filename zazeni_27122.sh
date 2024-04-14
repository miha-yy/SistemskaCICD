#!/bin/bash

docker pull mihayy9/sistemska:latest

docker run -d --name cicd mihayy9/sistemska:latest

echo "Container cicd is running using image mihayy9/sistemska:latest"