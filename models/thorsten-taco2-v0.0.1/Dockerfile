# Adapted from @thorstenMueller's training script (https://github.com/thorstenMueller/TTS_recipes)
# Docker file by @repodiac (https://github.com/repodiac/tit-for-tat/thorsten-tts)
# *** Use without warranty and at your own risk! ***

# Installation folder **inside** Docker container
# (NOTE: if it is changed to another folder, you have to manually change it to the same folder in the last line, ENTRYPOINT ...)
ARG BASEDIR=/tmp/tts

FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel as ttts-base
ARG BASEDIR
WORKDIR $BASEDIR

# Install system libraries etc.
FROM ttts-base as ttts1
ARG BASEDIR
WORKDIR $BASEDIR

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc espeak-ng espeak-ng-data git git-extras
RUN pip install pip --upgrade
RUN pip install gdown

# Clone deep-learning-german-tts repo and copy config and test sentences
RUN git clone --single-branch --branch dev https://github.com/thorstenMueller/deep-learning-german-tts.git
RUN cp $BASEDIR/deep-learning-german-tts/models/thorsten-taco2-v0.0.1/de-test-sentences.txt $BASEDIR
RUN cp $BASEDIR/deep-learning-german-tts/models/thorsten-taco2-v0.0.1/config.json $BASEDIR

# Download and extract "thorsten-TTS" dataset
FROM ttts1 as ttts2
ARG BASEDIR
WORKDIR $BASEDIR

RUN cd $BASEDIR
RUN gdown https://drive.google.com/uc?id=1yKJM1LAOQpRVojKunD9r8WN_p5KzBxjc -O thorsten-dataset.tgz
RUN tar -xvzf thorsten-dataset.tgz

# Prepare shuffled training and validate data (90% train, 10% val)
RUN shuf LJSpeech-1.1/metadata.csv > LJSpeech-1.1/metadata_shuf.csv
RUN head -n 20400 LJSpeech-1.1/metadata_shuf.csv > LJSpeech-1.1/metadata_train.csv
RUN tail -n 2268 LJSpeech-1.1/metadata_shuf.csv > LJSpeech-1.1/metadata_val.csv

# Install Mozilla TTS repo and dependencies
FROM ttts2 as ttts3
ARG BASEDIR
WORKDIR $BASEDIR

RUN git clone --single-branch --branch dev https://github.com/mozilla/TTS $BASEDIR/TTS

WORKDIR $BASEDIR/TTS
RUN python setup.py develop

# Add german phoneme cleaner library by @repodiac
FROM ttts3 as ttts4
ARG BASEDIR

RUN git clone https://github.com/repodiac/german_transliterate  $BASEDIR/german_transliterate
WORKDIR $BASEDIR/german_transliterate
RUN pip install -e .

WORKDIR $BASEDIR/TTS/mozilla_voice_tts/tts/utils/text
RUN sed '/import re/a from german_transliterate.core import GermanTransliterate' cleaners.py >> cleaners-new.py
RUN mv cleaners-new.py cleaners.py
RUN echo "\ndef german_phoneme_cleaners(text):" >> cleaners.py
RUN echo "\treturn GermanTransliterate(replace={';': ',', ':': ' '}, sep_abbreviation=' -- ').transliterate(text)" >> cleaners.py

# Run training
WORKDIR $BASEDIR/TTS/mozilla_voice_tts/bin/
ENTRYPOINT CUDA_VISIBLE_DEVICES="0" python train_tts.py --config_path $BASEDIR/config.json
