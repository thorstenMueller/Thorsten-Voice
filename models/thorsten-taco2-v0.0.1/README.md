> Steps taken from https://github.com/repodiac/tit-for-tat/tree/master/thorsten-TTS

> Hier reinzukopieren und/oder auf Repo von repodiac verweisen?


# Steps to start training as docker container

* git clone --single-branch --branch dev https://github.com/thorstenMueller/deep-learning-german-tts.git
* cd models/thorsten-taco2-v0.0.1
* docker build --rm -t thorsten-tts-training .
* ...

Thanks to @repodiac for providing Dockerfile. Please see https://github.com/repodiac/tit-for-tat/tree/master/thorsten-TTS