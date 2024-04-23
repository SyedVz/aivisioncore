param ([switch]$run_jetson=$False)

if ($build_jetson) {
    $script:NAME='c2x_jetson'
}
else {
    $script:NAME='c2x'
}

docker run --gpus all `
    -e RTSP_URL_DEMO_DOOR_OC=http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg `
    -e MEDIA_STORE_HOST=http://host.docker.internal `
    -e MEDIA_STORE_PORT=9090 `
    -e ACCOUNT_ID=test_acc `
    -e SOURCE_ID=00075fca-f8fa-faf8-ca5f-0700075fca5f `
    -e APPLICATION_ID=test_app `
    -v .:/app/out_dir ${NAME}:latest