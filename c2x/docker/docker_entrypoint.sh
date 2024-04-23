#!/bin/bash

set -e

video=${RTSP_URL_DEMO_DOOR_OC}

echo "Video URL: ${video}"

# ping http://host.docker.internal/
python3 -m c2x.test -v ${video} --headless --thingspace --threaded