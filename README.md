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
    python3 -m pip install -r .\requirements.txt
    ```

    For CV2X, some libraries are different from the above. So, in a separate python environment install cv2x imp requirements
     ```bash
    python3 -m pip install -r .\requirements_imp.txt
    ```

2. Run the test script from one level above this dir

    ```bash
    python3 -m c2x.test -v {path to video}
    ```

    e.g.:
    For camera input (cam idx 0):
    ```bash
    python3 -m c2x.test -v 0
    ```
    For video/stream input:
    ```bash
    python3 -m c2x.test -v 'http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg
    ```

    To get help on available options, run:
    ```bash
    python3 -m c2x.test --help
    ```
    
3. Start the car (to publish bsms and to listen to vision events)

    ```bash
    python3 -m imp_core.start_driving
    ```

Note: For Step 3: 
    (a) If using imp-lite, please make sure your public IP is whitelisted in imp-lite (if that is used as the imp server)
    (b) If using vzmode, make sure you are connected to a 5G network (or through a 5G hotspot)
    (c) For vzmode, you can monitor the car's movement in the following link:
        http://vzmode.las.wl.dltdemo.io:30888/

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
