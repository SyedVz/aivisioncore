# C2X Project

This project contains the codebase for c2x

## Structure
|Directory|Description|
|---|---|
|assets|Model checkpoints, etc.|
|base|Contains base classes for data structures/processors|
|docker|Dockerfile, entrypoint, etc.|
|imp_platform|IMP platform specific files|
|models|Implementations of detection/segmentation models|
|thingspace|ThingSpace platform specific files|

## Running the demo
### Command line
1. Install the requirements (one time)

    ```bash
    python -m pip install -r .\requirements.txt
    ```
2. Run the test script from one level above this dir

    ```bash
    python -m c2x.test -v {path to video}
    ```

    e.g.:
    For camera input (cam idx 0):
    ```bash
    python -m c2x.test -v 0
    ```
    For video/stream input:
    ```bash
    python -m c2x.test -v 'http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg
    ```

    To get help on available options, run:
    ```bash
    python -m c2x.test --help
    ```

### Docker
The testapp can be run as a docker container
1. Build docker image using the relevant script:

    PowerShell
    ```powershell
    cd c2x
    .\build_docker.ps1
    ```
    Bash
    ```bash
    cd c2x
    ./build_docker.sh
    ```
2. Run docker container using the relevant script:

    PowerShell
    ```powershell
    cd c2x
    .\run_docker.ps1
    ```
    Bash
    ```bash
    cd c2x
    ./run_docker.sh
    ```
