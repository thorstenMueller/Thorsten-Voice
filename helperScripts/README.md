# Short collection of helpful scripts for dataset creation and/or TTS training stuff

## MRS2LJSpeech
Python script which takes recordings (filesystem and sqlite db) done with Mycroft Mimic-Recording-Studio (https://github.com/MycroftAI/mimic-recording-studio) and creates an audio optimized dataset in widely supported LJSpeech directory structure.

Peter Schmalfeldt (https://github.com/manifestinteractive) did an amazing job as he optimized my originally (quick'n dirty) version of that script, so thank you Peter :-)
See more details here: https://gist.github.com/manifestinteractive/6fd9be62d0ede934d4e1171e5e751aba#file-mrs2ljspeech-py

## Dockerfile.Jetson-Coqui
> Add your user to `docker` group to not require sudo on all operations.

Thanks to NVIDIA for providing docker images for Jetson platform. I use the "machine learning (ML)" image as baseimage for setting up a Coqui environment.

> You can use any branch or tag as COQUI_BRANCH argument. v0.1.3 is just the current stable version.

Switch to directory where Dockerfile is in and run `nvidia-docker build . -f Dockerfile.Jetson-Coqui --build-arg COQUI_BRANCH=v0.1.3 -t jetson-coqui` to build your container image. When build process is finished you can start a container on that image.


### Mapped volumes
We need to bring your dataset and configuration file into our container so we should map a volume on running container
`nvidia-docker run -p 8888:8888 -d --shm-size 32g --gpus all -v [host path with dataset and config.json]:/coqui/TTS/data jetson-coqui`. Now we have a running container ready for Coqui TTS magic.

### Jupyter notebook
Coqui provides lots of useful Jupyter notebooks for dataset analysis. Once your container is up and running you should be able to call 

### Running bash into container
`nvidia-docker exec -it jetson-coqui /bin/bash` now you're inside the container and an `ls /coqui/TTS/data` should show your dataset files.