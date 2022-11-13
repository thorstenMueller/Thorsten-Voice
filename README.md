![Thorsten-Voice logo](Logo_Thorsten-Voice.png)

- [Project motivation](#motivation-for-thorsten-voice-project-speaking_head-speech_balloon)
  
- [Personal note](#some-personal-words-before-using-thorsten-voice)

- [**Thorsten** Voice Datasets](#voice-datasets)
  - [Thorsten-21.02-neutral](#thorsten-2102-neutral)
  - [Thorsten-21.06-emotional](#thorsten-2106-emotional)
  - [Thorsten-22.10-neutral](#thorsten-2210-neutral)

- [**Thorsten** TTS-Models](#tts-models)
  - [Thorsten-21.04-Tacotron2-DCA](#thorsten-2104-tacotron2-dca)
  - [Thorsten-22.05-VITS](#thorsten-2205-vits)
  - [Thorsten-22.08-Tacotron2-DDC](#thorsten-2208-tacotron2-ddc)
  - [Other models](#other-models)
  
- [Public talks](#public-talks)

- [My Youtube channel](#youtube-channel)

- [Special Thanks](#thanks-section)


# Motivation for Thorsten-Voice project :speaking_head: :speech_balloon:
A **free** to use, **offline** working, **high quality** **german** **TTS** voice should be available for every project without any license struggling.

<a href="https://twitter.com/intent/follow?screen_name=ThorstenVoice"><img src="https://img.shields.io/twitter/follow/ThorstenVoice?style=social&logo=twitter" alt="follow on Twitter"></a>
[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCjqqTVVBTsxpm0iOhQ1fp9g?style=social)](https://www.youtube.com/c/ThorstenMueller)
[![Project website](https://img.shields.io/badge/Project_website-www.Thorsten--Voice.de-92a0c0)](https://www.Thorsten-Voice.de)

# Some personal words before using **Thorsten-Voice**
> I contribute my voice as a person believing in a world where all people are equal. No matter of gender, sexual orientation, religion, skin color and geocoordinates of birth location. A global world where everybody is warmly welcome on any place on this planet and open and free knowledge and education is available to everyone. :earth_africa: (*Thorsten Müller*)

Please keep in mind, that **i am no professional voice talent**. I'm just a normal guy sharing his voice with the world.

# Voice-Datasets
Voice datasets are listed on Zenodo:
| Dataset         | DOI Link                                                                                                            |
| --------------- | ------- |
| Thorsten-21.02-neutral | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5525342.svg)](https://doi.org/10.5281/zenodo.5525342) |
| Thorsten-21.06-emotional | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5525023.svg)](https://doi.org/10.5281/zenodo.5525023) |
| Thorsten-22.10-neutral | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7265581.svg)](https://doi.org/10.5281/zenodo.7265581) |

## Thorsten-21.02-neutral
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5525342.svg)](https://doi.org/10.5281/zenodo.5525342)

```
@dataset{muller_thorsten_2021_5525342,
  author       = {Müller, Thorsten and
                  Kreutz, Dominik},
  title        = {Thorsten-Voice - "Thorsten-21.02-neutral" Dataset},
  month        = feb,
  year         = 2021,
  note         = {{Please use it to make the world a better place for 
                   whole humankind.}},
  publisher    = {Zenodo},
  version      = {3.0},
  doi          = {10.5281/zenodo.5525342},
  url          = {https://doi.org/10.5281/zenodo.5525342}
}
```

> :speaking_head: **Listen to some audio recordings from this dataset [here](https://drive.google.com/drive/folders/1KVjGXG2ij002XRHb3fgFK4j0OEq1FsWm?usp=sharing).**

### Dataset summary
* Recorded by Thorsten Müller
* Optimized by Dominik Kreutz
* LJSpeech file and directory structure
* 22.668 recorded phrases (*wav files*)
* More than 23 hours of pure audio
* Samplerate 22.050Hz
* Mono
* Normalized to -24dB
* Phrase length (min/avg/max): 2 / 52 / 180 chars
* No silence at beginning/ending
* Avg spoken chars per second: 14
* Sentences with question mark: 2.780
* Sentences with exclamation mark: 1.840

### Dataset evolution
As described in the PDF document ([evolution of thorsten dataset](./EvolutionOfThorstenDataset.pdf)) this dataset consists of three recording phases.

* **Phase 1**: Recorded with a cheap usb microphone (*low quality*)
* **Phase 2**: Recorded with a good microphone (*good quality*)
* **Phase 3**: Recorded with same good microphone but longer phrases (> 100 chars) (*good quality*)

If you want to use a dataset subset you can see which files belong to which recording phase in [recording quality](./RecordingQuality.csv) csv file.


## Thorsten-21.06-emotional
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5525023.svg)](https://doi.org/10.5281/zenodo.5525023)

```
@dataset{muller_thorsten_2021_5525023,
  author       = {Müller, Thorsten and
                  Kreutz, Dominik},
  title        = {{Thorsten-Voice - "Thorsten-21.06-emotional" 
                   Dataset}},
  month        = jun,
  year         = 2021,
  note         = {{Please use it to make the world a better place for 
                   whole humankind.}},
  publisher    = {Zenodo},
  version      = {2.0},
  doi          = {10.5281/zenodo.5525023},
  url          = {https://doi.org/10.5281/zenodo.5525023}
}
```

All emotional recordings where recorded by myself and i tried to feel and pronounce that emotion even if the phrase context does not match that emotion. Example: I pronounced the sleepy recordings in the tone i have shortly before falling asleep.

### Samples
Listen to the phrase "**Mist, wieder nichts geschafft.**" in following emotions.

* :slightly_smiling_face: [Neutral](./samples/thorsten-21.06-emotional/neutral.wav)
* :nauseated_face: [Disgusted](./samples/thorsten-21.06-emotional/disgusted.wav)
* :angry: [Angry](./samples/thorsten-21.06-emotional/angry.wav)
* :grinning: [Amused](./samples/thorsten-21.06-emotional/amused.wav)
* :astonished: [Surprised](./samples/thorsten-21.06-emotional/surprised.wav)
* :pensive: [Sleepy](./samples/thorsten-21.06-emotional/sleepy.wav)
* :dizzy_face: [Drunk](./samples/thorsten-21.06-emotional/drunk.wav)
* 🤫 [Whispering](./samples/thorsten-21.06-emotional/whisper.wav)
### Dataset summary
* Recorded by Thorsten Müller
* Optimized by Dominik Kreutz
* 300 sentences * 8 emotions = 2.400 recordings
* Mono
* Samplerate 22.050Hz
* Normalized to -24dB
* No silence at beginning/ending
* Sentence length: 59 - 148 chars


## Thorsten-22.10-neutral
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7265581.svg)](https://doi.org/10.5281/zenodo.7265581)
> :speaking_head: **Listen to some audio recordings from this dataset [here](https://drive.google.com/drive/folders/1dxoSo8Ktmh-5E0rSVqkq_Jm1r4sFnwJM?usp=sharing).**

```
@dataset{muller_thorsten_2022_7265581,
  author       = {Müller, Thorsten and
                  Kreutz, Dominik},
  title        = {ThorstenVoice Dataset 2022.10},
  month        = oct,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.7265581},
  url          = {https://doi.org/10.5281/zenodo.7265581
}
```

# TTS Models

## Thorsten-21.04-Tacotron2-DCA
This [TTS-model](https://drive.google.com/drive/folders/1m4RuffbvdOmQWnmy_Hmw0cZ_q0hj2o8B?usp=sharing) has been trained on [**Thorsten-21.02-neutral**](#thorsten-2102-neutral) dataset. The recommended trained Fullband-MelGAN Vocoder can be downloaded [here](https://drive.google.com/drive/folders/1hsfaconm4Yd9wPVyOtrXjWQs4ZAPoouY?usp=sharing).

Run the model:
* pip install TTS==0.5.0
* tts-server --model_name tts_models/de/thorsten/tacotron2-DCA


## Thorsten-22.05-VITS
Trained on dataset **Thorsten-22.05-neutral**.
Audio samples are available on [Thorsten-Voice website](https://www.thorsten-voice.de/en/just-get-started/).

To run TTS server just follow these steps:
* pip install tts==0.7.1
* tts-server --model_name tts_models/de/thorsten/vits
* Open browser on http://localhost:5002 and enjoy playing

## Thorsten-22.08-Tacotron2-DDC
Trained on dataset [**Thorsten-22.05-neutral**](#thorsten-2205-neutral).
Audio samples are available on [Thorsten-Voice website]([https://www.thorsten-voice.de/en/just-get-started/](https://www.thorsten-voice.de/2022/08/14/welches-tts-modell-klingt-besser/)).

To run TTS server just follow these steps:
* pip install tts==0.8.0
* tts-server --model_name tts_models/de/thorsten/tacotron2-DDC
* Open browser on http://localhost:5002 and enjoy playing


## Other models
### Silero

You can use a free A-GPL licensed models trained on **Thorsten-21.02-neutral** dataset via the [silero-models](https://github.com/snakers4/silero-models/blob/master/models.yml) project.

* [Thorsten 16kHz](https://drive.google.com/drive/folders/1tR6w4kgRS2JJ1TWZhwoFuU04Xkgo6YAs?usp=sharing)
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples_tts.ipynb)

### ZDisket
[ZDisket](https://github.com/ZDisket/TensorVox) made a tool called TensorVox for setting up an TTS environment on Windows and included a german TTS model trained by [monatis](https://github.com/monatis/german-tts). Thanks for sharing that :thumbsup:. See it in action on [Youtube](https://youtu.be/tY6_xZnkv-A).

# Public talks
I really want to bring the topic "**Open Voice For An Open Future**" to a bigger public attention.

* I've been part of a Linux User Group podcast about Mycroft AI and talked on my TTS efforts on that in (*May 2021*).
* I was invited by [Yusuf](https://github.com/monatis/) from Turkish tensorflow community to talk on "How to make machines speak with your own voice". This talk has been streamed live on Youtube and is available [here](https://www.youtube.com/watch?v=m-Uwb-Bg144&t=2303s). If you're interested on the showed slides, feel free to download my presentation [here](https://docs.google.com/presentation/d/1ynnw0ilKV3WwMSJHytrN3GXRiFr8x3r0DUimBm1y0LI/edit?usp=sharing) (*June 2021*)
)
* I've been invited as speaker on VoiceLunch language & linguistics on 03.01.2022. [Here are my slides](https://docs.google.com/presentation/d/1Gi6BmYHs7g4ZgdAiIKGBnBwZDCvJOD9DJxQOGlgds1o/edit?usp=sharing) (*January 2022*).

# Youtube channel
In summer 2021 i've started to share my lessons learned and experiences on open voice tech, in special **TTS** on my little [Youtube channel](https://www.youtube.com/c/ThorstenMueller). If you check out and like my videos i'd happy to welcome you as subscriber and member of my little Youtube community.


# Feel free to file an issue if you ...
* Use my TTS voice in your project(s)
* Want to share your trained "Thorsten" model
* Get to know about any abuse usage of my voice

# Thanks section
## Cool projects
* https://commonvoice.mozilla.org/
* https://coqui.ai/
* https://mycroft.ai/
* https://github.com/rhasspy/

## Cool people
* [El-Tocino](https://github.com/el-tocino/)
* [Eren Gölge](https://github.com/erogol/)
* [Gras64](https://github.com/gras64/)
* [Kris Gesling](https://github.com/krisgesling/)
* [Nmstoker](https://github.com/nmstoker)
* [Othiele](https://discourse.mozilla.org/u/othiele/summary)
* [Repodiac](https://github.com/repodiac)
* [SanjaESC](https://github.com/SanjaESC)
* [Synesthesiam](https://github.com/synesthesiam/)

## Even more special people
Additionally, a really nice thanks for my dear colleague, Sebastian Kraus, for supporting me with audio recording equipment and for being the creative mastermind behind the logo design.

And last but not least i want to say a **huge, huge thank you** to a special guy who supported me on this journey as a partner right from the beginning. Not just with nice words, but with his time, audio optimization knowhow and finally GPU power. 

**Thank you so much, dear **Dominik** ([@domcross](https://github.com/domcross/)) for being my partner on this journey.**

Thorsten (*Twitter: @ThorstenVoice*)
