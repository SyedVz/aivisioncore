set -e

PLATFORM_AMD64='nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04'
PLATFORM_JETSON='nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3'
PLATFORM_IMAGE=${PLATFORM_AMD64} #${PLATFORM_JETSON}
PLATFORM_NAME=c2x #c2x_jetson

docker build -t ${PLATFORM_NAME}:latest --progress=plain --build-arg PLATFORM_IMAGE=${PLATFORM_IMAGE} \
    -f ./docker/Dockerfile .