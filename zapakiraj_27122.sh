#!/bin/bash

echo "${ACCESS_TOKEN}" | docker login --username "${USERNAME}" --password-stdin

docker build -t "${USERNAME}/sistemska:${GITHUB_SHA}" .
docker push "${USERNAME}/sistemska:${GITHUB_SHA}"

docker build -t "${USERNAME}/sistemska:latest" .
docker push "${USERNAME}/sistemska:latest"