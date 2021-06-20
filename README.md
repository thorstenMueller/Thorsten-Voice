![Thorsten - Open German Voice Dataset](./img/ThorstenVoice_Logo_Small.png "Thorsten - Open German Voice Dataset")

- [Introduction to "Thorsten-Voice" :speaking_head: :speech_balloon: :sloth:](#introduction-to-thorsten-voice-speaking_head-speech_balloon-sloth)
  
- [A personal note](#please-read-some-personal-words-before-using-dataset--tts-models)

- [Voice "Thorsten" (neutral)](#dataset-thorsten-neutral)
  - [Samples of my neutral voice](#samples-of-my-neutral-voice)
  - [Dataset information :microphone:](#dataset-information-microphone)
  - [Dataset evolution / changelog](#dataset-evolution)
  - [Download information](#neutral-dataset-download-information)

- [Voice "Thorsten" (emotional)](#dataset-Thorsten-emotional)
  - [Emotional dataset information and samples :microphone:](#emotional-dataset-information-and-samples-microphone)
  - [Emotional dataset download information](#emotional-dataset-download-information)

- [Pretrained TTS models](#pretrained-tts-models)
  - [Coqui models](#coqui-models)
  - [Pre-trained Silero-models](#silero-models)

- [Public talks](#public-talks)

- [Feel free to file an issue if you ...](#feel-free-to-file-an-issue-if-you-)
- [Recommended projects / communities](#recommended-projects)
- [Special thanks](#special-thanks)
- [Additional links](#additional-links)


# Introduction to "Thorsten-Voice" :speaking_head: :speech_balloon: :sloth:
## **A free to use, offline working, high quality german TTS voice should be available for every project without any license struggling.**

[![CC-0 license](https://img.shields.io/badge/License-CC--0-blue.svg)](https://creativecommons.org/licenses/by-nd/4.0)
![Maintaner](https://img.shields.io/badge/maintainer-Thorsten_Mueller-blue)
<a href="https://twitter.com/intent/follow?screen_name=ThorstenVoice">
        <img src="https://img.shields.io/twitter/follow/ThorstenVoice?style=social&logo=twitter"
            alt="follow on Twitter"></a>
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Audio comparison page](https://img.shields.io/badge/Audio_samples-TTS_comparison-92a0c0)](https://thorstenmueller.github.io/deep-learning-german-tts/audio_compare)

**A summary of my open german voice dataset is available on Wikipedia**

[https://de.wikipedia.org/wiki/Thorsten_(Stimme)](https://de.wikipedia.org/wiki/Thorsten_(Stimme)) :smiley: 

Speaking tech devices and voice based smart assistants are very popular ourdays. But for providing nice sounding TTS lot of projects depend on big tech cloud services for synthezing voice. While quality is quite good, there remain critical aspects like **privacy concerns** and **missing offline availablitiy**.

## True, but what is this all about
> I want to (*hopefully*) fill that german TTS gap and make the most personal contribution i can give.<br>
**I contribute my personal voice!** :green_heart:

## This contribution is split into three parts:
* "Thorsten" **neutral** dataset
* "Thorsten" **emotional** dataset
* Pretrained TTS models based on "Thorsten" dataset

# Please read some personal words before using dataset / TTS models
> I contribute my voice as a person believing in a world where all people are equal. No matter of gender, sexual orientation, religion, skin color and geocoordinates of birth location. A global world where everybody is warmly welcome on any place on this planet and open and free knowledge and education is available to everyone. :earth_africa:

**So hopefully my voice is used in this manner to make this world a better place for all of us :smiley:.**

**tl;dr** Please don't use for evil!

# Datasets


> For both datasets please keep in mind, that **i am no professional voice talent**. I'm just a normal guy sharing his voice with you.

## Dataset "Thorsten" neutral
### Samples of my neutral voice
To get an impression what my voice sounds to decide if it fits to your project i published some sample recordings, so no need to download complete dataset first.

* [Das Teilen eines Benutzerkontos ist strengstens untersagt.](./samples/original_recording/recorded_sample_01.wav )
* [Der Prophet spricht stets in Gleichnissen.](./samples/original_recording/recorded_sample_02.wav )
* [Bitte schmeißt euren Müll nicht einfach in die Walachei.](./samples/original_recording/recorded_sample_03.wav )
* [So etwas würde mir nie in den Sinn kommen.](./samples/original_recording/recorded_sample_04.wav )
* [Sie klettert auf einen Stein und nimmt eine Denkerpose ein.](./samples/original_recording/recorded_sample_05.wav )
* [Jede gute Küchenwaage hat eine Tara-Funktion.](./samples/original_recording/recorded_sample_06.wav )
* [Jeden Gedanken kannst du hier loswerden.](./samples/original_recording/recorded_sample_07.wav )

### Dataset information :microphone:

* ljspeech-1.1 structure
* 22.668 recorded phrases (wav files)
* more than 23 hours of pure audio
* samplerate 22.050Hz
* mono
* normalized to -24dB
* phrase length (min/avg/max): 2 / 52 / 180 chars
* no silence at beginning/ending
* avg spoken chars per second: 14
* sentences with question mark: 2.780
* sentences with exclamation mark: 1.840

![text length vs. mean audio duration](./img/thorsten-de---datasetAnalysis1.png)
![text length vs. median audio duration](./img/thorsten-de---datasetAnalysis2.png)
![text length vs. STD](./img/thorsten-de---datasetAnalysis3.png)
![text length vs. number instances](./img/thorsten-de---datasetAnalysis4.png)
![signal noise ratio](./img/thorsten-de---datasetAnalysis5.png)
![bokeh](./img/thorsten-de---datasetAnalysis6.png)

### Dataset evolution
As described in the pdf document ([evolution of thorsten dataset](./EvolutionOfThorstenDataset.pdf)) this dataset consists of three recording phases.

* **phase1**: Recorded with a cheap usb microphone
* **phase2**: Recorded with a good microphone
* **phase3**: Recorded with same good microphone but longer phrases (> 100 chars)

If you wanna use just a dataset subset (phase1 and/or phase2 and/or phase3) you can see which files belong to which recording phase in [recording quality](./RecordingQuality.csv) csv file.


### Neutral dataset download information
> Download size: 2,7GB

| Version         | Description                                                                                       | Date       | Link                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| thorsten-de-v01 | Initial version                                                                                   | 2020-06-28 | [Google Drive Download v01](https://drive.google.com/file/d/1yKJM1LAOQpRVojKunD9r8WN_p5KzBxjc/view?usp=sharing) |
| thorsten-de-v02 | Normalized to -24dB and split metadata.csv into shuffeled metadata_train.csv and metadata_val.csv | 2020-08-22 | [Google Drive Download v02](https://drive.google.com/file/d/1mGWfG0s2V2TEg-AI2m85tze1m4pyeM7b/view?usp=sharing) |
| thorsten-de-v03 | Based on v02 dataset, but with increased speed by 10% (using ffmpeg atempo=1.1).                  | 2021-02-10 | [Google Drive Download v03](https://drive.google.com/file/d/134_UramfCRoAxRrOnhbPJ2YHHTwxRtr-/view?usp=sharing) |


## Dataset "Thorsten" emotional
### Emotional dataset information and samples :microphone:
* 300 sentences * 8 emotions = 2.400 recordings
* recorded by Thorsten Müller (optimized by Dominik Kreutz)
* mono
* samplerate 22.050Hz
* normalized to -24dB
* no silence at beginning/ending
* sentence length: 59 - 148 chars

*Btw. i mentioned, that i'm no professional voice talent, did i?*
> "Mist, wieder nichts geschafft."

| Emotion   | Minutes | Sample |
|-----------|---------| --------- | 
| Neutral :slightly_smiling_face:    | 19 min. | [neutral sample](./samples/emotional_recording/neutral.wav) |
| Disgusted :nauseated_face: | 23 min. | [disgusted sample](./samples/emotional_recording/disgusted.wav) |
| Angry :angry:    | 20 min. | [angry sample](./samples/emotional_recording/angry.wav) |
| Amused :grinning:    | 18 min. | [amused sample](./samples/emotional_recording/amused.wav) |
| Surprised :astonished: | 18 min. | [surprised sample](./samples/emotional_recording/surprised.wav) |
| Sleepy :pensive:    | 30 min. | [sleepy sample](./samples/emotional_recording/sleepy.wav) |
| Drunk (*i was "not" drunk while recording!*) :dizzy_face:    | 25 min. | [drunk sample](./samples/emotional_recording/drunk.wav) |
| Whispering 🤫    | 22 min. | [whispering sample](./samples/emotional_recording/whisper.wav) |

### Emotional dataset download information
> Download size: 350MB

| Version         | Description                                                                                       | Date       | Link                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| thorsten-de-emotional-v01 | Initial version                                                                                   | 2021-04-03 | [Google Drive Download v01](https://drive.google.com/file/d/1fm2IqXMLr6jaZCgG_Mt4vq_O3ZubiIQ6/view?usp=sharing) |
| thorsten-de-emotional-v02 | Added emotions "drunk" and "whispering" version                                                                                   | 2021-06-13 | [Google Drive Download v02](https://drive.google.com/file/d/1FBZ4Cb4TQGwZiAzzj41yTBsdGp7yRQbS/view?usp=sharing) |


# Pretrained TTS models
If you trained a model on "Thorsten" dataset please file an issue with some information on it. Sharing a trained model is highly appreciated.

My personal training sessions are based on TTS repo code (originally initiated by Mozilla) and now maintained through https://www.coqui.ai (:frog:)
## Coqui models

### Easy pip install
For all "Thorsten" coqui models i recommend setting up a virtual environment (*venv*).
* mkdir ThorstenVoice
* cd ThorstenVoice
* python3 -m venv .
* source ./bin/activate
* pip install -U pip
* pip install -U tts
* tts --list

> tts-server --model_name tts_models/de/thorsten/tacotron2-DCA

or

> tts-server --model_name tts_models/de/thorsten/tacotron2-DCA --vocoder_name vocoder_models/universal/libri-tts/fullband-melgan 

* Open web-browser on http://localhost:5002

Check details here: > see: https://github.com/coqui-ai/TTS/releases/tag/v0.0.11


### Download Coqui trained checkpoints / config
| Model name | Coqui Repo branch / commit | Release date | Google Drive Download Link |
|----------------------------------|---------------------------------------------------|----------------------|--------------------------------------------------------------------------------------|
| Thorsten Tacotron2 DCA           | master / 0ee3eeefb553678d56c49534f3972a426a254649 | 2021-04-02           | [Google Drive Thorsten Taco2 DCA](https://drive.google.com/drive/folders/1m4RuffbvdOmQWnmy_Hmw0cZ_q0hj2o8B?usp=sharing) |
| Thorsten Vocoder WaveGrad        | master / 0ee3eeefb553678d56c49534f3972a426a254649 | 2021-04-02           | [Google Drive Thorsten Vocoder WaveGrad](https://drive.google.com/drive/folders/1uOWpYH3yoDv5_3Dn_aDbAprEmyk1tDw5?usp=sharing) |
| Thorsten Vocoder Fullband-MelGAN | master / 0ee3eeefb553678d56c49534f3972a426a254649 | training-in-progress | training-in-progress                                                                 |
| Thorsten Vocoder HifiGAN         |                                                   | planned              | planned                                                                              |
| Thorsten Vocoder WaveRNN         |                                                   | planned              | planned                                                                              |

## Silero-models

You can use a free A-GPL licensed models trained on this dataset via the [silero-models](https://github.com/snakers4/silero-models) project. The full list of models including their older version is available via this [yaml file](https://github.com/snakers4/silero-models/blob/master/models.yml).

| Speaker        | Gender | Language | Examples                                                                                                                                                                                     | Colab                                                                                                                                                                        |
| -------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| thorsten_8khz  | m      | de       | [8000](https://drive.google.com/drive/folders/1mpQCK5E_IqhcSurnYuGePJiJWL4ZL08z?usp=sharing) / [16000](https://drive.google.com/drive/folders/1tR6w4kgRS2JJ1TWZhwoFuU04Xkgo6YAs?usp=sharing) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb) |
| thorsten_16khz | m      | de       | [8000](https://drive.google.com/drive/folders/1mpQCK5E_IqhcSurnYuGePJiJWL4ZL08z?usp=sharing) / [16000](https://drive.google.com/drive/folders/1tR6w4kgRS2JJ1TWZhwoFuU04Xkgo6YAs?usp=sharing) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb) |


# Public talks
> I really want to bring the topic "OpenVoice" to a bigger public attention, so i am happy to be invited as a speaker on that.

I have been part of a Linux User Group podcast about Mycroft AI and talked on my TTS efforts on that in May 2021. I'll publish a link to that talk when it's released to the public.

In addition to that i was invited by [Yusuf](https://github.com/monatis/) from Turkish tensorflow community to talk on "How to make machines speak with your own voice" on june 2nd, 2021. This talk has been streamed live on Youtube and is available [here](https://www.youtube.com/watch?v=m-Uwb-Bg144&t=2303s).
If you're interested on the showed slides, feel free to download my presentation [here](https://docs.google.com/presentation/d/1ynnw0ilKV3WwMSJHytrN3GXRiFr8x3r0DUimBm1y0LI/edit?usp=sharing)

# Feel free to file an issue if you ...
* have improvements on dataset
* use my TTS voice in your project(s)
* want to share your trained "Thorsten" model
* get to know about any abuse usage of my voice

# Recommended projects
* https://mycroft.ai/ (*for building an opensource privacy friendly voice assistant*)
* https://www.mozilla.org (*for initiating voice projects for STT and TTS*)
* https://coqui.ai/ (*for keeping voice projects running*)
* https://github.com/coqui-ai/TTS
* https://github.com/TensorSpeech/TensorFlowTTS
* https://github.com/rhasspy/de_larynx-thorsten

# Special thanks
I want to thank all open source communities for providing great projects.

Just to name some nice guys who joined me on this TTS roadtrip:

* eltocino (https://github.com/el-tocino/)
* erogol (https://github.com/erogol/)
* gras64 (https://github.com/gras64/)
* krisgesling (https://github.com/krisgesling/)
* nmstoker (https://github.com/nmstoker)
* othiele (https://discourse.mozilla.org/u/othiele/summary)
* repodiac (https://github.com/repodiac)
* SanjaESC (https://github.com/SanjaESC)

Additionally, a really nice thanks for my dear colleague, Sebastian Kraus, for supporting me with audio recording equipment and for being the creative mastermind behind the logo design.

And last but not least i want to say a huge thank you to a special guy who supported me on this journey right from the beginning. Not just with nice words, but with his time, audio optimization knowhow and finally his gpu computing power. 

Without his amazing support this dataset (in it's current way) would not exists.

Thank you Dominik (@domcross / https://github.com/domcross/)

# Additional links
* https://medium.com/@thorsten_Mueller/why-ive-chosen-to-donate-my-german-voice-for-mankind-177beeb91675
* https://discourse.mozilla.org/t/contributing-my-german-voice-for-tts/48150
* https://community.mycroft.ai/
* https://github.com/MycroftAI/mimic-recording-studio

We'll hear us in future :speaking_head:

Thorsten
(https://twitter.com/ThorstenVoice)
