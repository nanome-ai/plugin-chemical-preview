#!/bin/bash

echo "./deploy.sh $*" > redeploy.sh
chmod +x redeploy.sh

existing=$(docker ps -aqf name=chemical-preview)
if [ -n "$existing" ]; then
    echo "removing existing container"
    docker rm -f $existing
fi

docker run -d \
--name chemical-preview \
--restart unless-stopped \
-e ARGS="$*" \
chemical-preview
