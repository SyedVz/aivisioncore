ARG PLATFORM_IMAGE=nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04

FROM ${PLATFORM_IMAGE}

WORKDIR /app

# RUN apt update && apt install -y python3 python3-pip ffmpeg \
#     libsm6 libxext6

RUN apt update && apt install -y --upgrade python3 python3-pip ffmpeg libsm6 libxext6

RUN python3 -m pip install --user -U pip setuptools 

RUN python3 -m pip install --user opencv-python-headless tqdm \
    transformers yolov7detect

ADD . /app/c2x/
ADD ./docker/docker_entrypoint.sh /app/
RUN chmod +x /app/docker_entrypoint.sh

RUN ls -al c2x

CMD ["./docker_entrypoint.sh"]
