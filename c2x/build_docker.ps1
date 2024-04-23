param ([switch]$build_jetson=$False)

$local:PLATFORM_AMD64='nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04'
$local:PLATFORM_JETSON='nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3'

if ($build_jetson) {
    $script:PLATFORM_IMAGE=${PLATFORM_JETSON}
    $script:NAME='c2x_jetson'
}
else {
    $script:PLATFORM_IMAGE=${PLATFORM_AMD64}
    $script:NAME='c2x'
}

Write-Output "Building ${NAME}"

docker build -t ${NAME}:latest --progress=plain `
    --build-arg PLATFORM_IMAGE=${PLATFORM_IMAGE} `
    -f ./docker/Dockerfile .