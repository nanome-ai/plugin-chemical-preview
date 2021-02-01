#!/bin/bash

if [ -n "$(docker ps -aqf name=nanome-chemical-preview)" ]; then
    echo "removing exited container"
    docker rm -f nanome-chemical-preview
fi

docker run -d \
--name nanome-chemical-preview \
--restart unless-stopped \
-e ARGS="$*" \
nanome-chemical-preview
