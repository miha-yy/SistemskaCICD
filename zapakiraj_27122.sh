#!/bin/bash

if [ -z "$USERNAME" ] || [ -z "$ACCESS_TOKEN" ] || [ -z "$GITHUB_SHA" ]; then
  echo "Error: One or more required environment variables are missing."
  exit 1
fi

echo "${ACCESS_TOKEN}" | docker login --username "${USERNAME}" --password-stdin

docker build -t "${USERNAME}/sistemska:${GITHUB_SHA}" .
docker push "${USERNAME}/sistemska:${GITHUB_SHA}"

docker build -t "${USERNAME}/sistemska:latest" .
docker push "${USERNAME}/sistemska:latest"