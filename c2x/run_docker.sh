docker run -it --rm --runtime nvidia \
    --network=infra_some-net \
    -e RTSP_URL_DEMO_DOOR_OC=http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg \
    -e MEDIA_STORE_HOST=http://media-store \
    -e MEDIA_STORE_PORT=9090 \
    -e ACCOUNT_ID=2171d850-9adc-63ab-ec67-c09b091b706a \
    -e SOURCE_ID=00075fca-f8fa-faf8-ca5f-0710075fca5f \
    -e APPLICATION_ID=test_app \
    -v .:/app/out_dir c2x_jetson:latest

# http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg
# https://video.deldot.gov/live/NCAM002.stream/playlist.m3u8
