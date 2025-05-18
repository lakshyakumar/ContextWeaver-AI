#!/bin/bash

set -e

docker build -t contextweaver-ai --platform linux/amd64 .

# Tag image
# docker tag contextweaver-ai registry/repo:tag

# Push image
# docker push registry/repo:tag

# Modify to select correct env file or mount it using docker-compose or kubernetes secrets 
docker run -p 8000:8000 --env-file env.sample contextweaver-ai
