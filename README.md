# Introduction
Many smart assistants like Amazon Alexa, Google Home, Apple Siri and Microsoft Cortana need an internet connection to offer the functions STT (speech in text) and TTS (text in speech) in decent quality. But there are also open source projects that develop alternative wizards, some of which work offline. Personally i'm playing currently around with MyCroft AI which has a great community.

For the area "STT / TTS", however, good training test data (eg for deep learning) are required. This is where the Mozilla Common Voice project comes into play.

# And?!
I want to make my small modest contribution and contribute the model (tacotron version 1 and 2) of my personal voice (**german**) to the community for free to use.

# Samples of my original voice
To get an impression of what my voice sounds to decide if it fits to your project i published some sample recordings. As soon the final model is available i'll upload some generated TTS samples too.

* [Das Teilen eines Benutzerkontos ist strengstens untersagt.](./samples/original_recording/recorded_sample_01.wav )
* [Der Prophet spricht stets in Gleichnissen.](./samples/original_recording/recorded_sample_02.wav )
* [Bitte schmeißt euren Müll nicht einfach in die Walachei.](./samples/original_recording/recorded_sample_03.wav )
* [So etwas würde mir nie in den Sinn kommen.](./samples/original_recording/recorded_sample_04.wav )
* [Sie klettert auf einen Stein und nimmt eine Denkerpose ein.](./samples/original_recording/recorded_sample_05.wav )
* [Jede gute Küchenwaage hat eine Tara-Funktion.](./samples/original_recording/recorded_sample_06.wav )
* [Jeden Gedanken kannst du hier loswerden.](./samples/original_recording/recorded_sample_07.wav )


# Dataset information
I recorded my voice using mimic-recording-studio by mycroft and a german corpus provided by @gras64. After recording and removing bad recordings, @domcross optimized the dataset concerning random noise, echo and background beeps.
Finally the dataset used for training is:

* 20.711 recorded phrases (wav files)
* more than 20 hours of pure audio
* samplerate 22.050Hz
* mono
* avg sentence length: 47 chars
* avg spoken chars per second: 14
* sentences with question mark: 2.759
* sentences with exclamation mark: 1.869
* ljspeech-1.1 structure

> TODO: Add bokeh graph.
Changing recording location and equipment duing the recording session leads to two clusters in recording bokeh.

# Training tacotron version 1 (for mimic2 usage)

## Graphs
### analyze output
![char_len_vs_avg_secs](./img/char_len_vs_avg_secs.png?raw=true "char_len_vs_avg_secs")
![char_len_vs_med_secs](./img/char_len_vs_med_secs.png?raw=true "char_len_vs_med_secs")
![char_len_vs_mode_secs](./img/char_len_vs_mode_secs.png?raw=true "char_len_vs_mode_secs")
![char_len_vs_num_samples](./img/char_len_vs_num_samples.png?raw=true "char_len_vs_num_samples")
![char_len_vs_std](./img/char_len_vs_std.png?raw=true "char_len_vs_std")

### alignment
> Training in progress - step 81k

![](./img/tacotron1-step-81000-align.png?raw=true "tacotron1-step-81000-align")

### Tensorboard
> Training in progress - step 81k

![](./img/tacotron1-tensorboard-01.png?raw=true "tacotron1-tensorboard-01")
![](./img/tacotron1-tensorboard-02.png?raw=true "tacotron1-tensorboard-02")

## TTS samples
> All samples are "training in progress"
* [Tacotron 1 training (Step 81.000)](./samples/tts_tacotron1/step-81000-audio.wav )

## Model release (tacotron 1)
> Will be released as soon training process is finished


# Mozilla TTS training/model (tacotron 2)

## Training info

## Model release (tacotron2)
> Will be released as soon training process is finished


# Special thanks
I want to thank the whole community for providing great open source products.

Special thanks go to
- domcross (https://github.com/domcross/)
- gras64 (https://github.com/gras64/)
- erogol (https://github.com/erogol/)
- krisgesling (https://github.com/krisgesling/)
- eltocino (https://chat.mycroft.ai)
- nmstroker from Mozilla forum

for their support or this.

A very special thank you for @domcross for his time, support, audio optimzing knowhow and finally his gpu computing power. Thank you :-)

# Finally
If you use my (concrete) TTS voice I would be grateful for an info about the project and a demo.

> Please do not use my voice for evil.

# TODO
- add training plots
- add bokeh graph
- google drive download urls for model download

# Links
* https://community.mycroft.ai/
* https://github.com/MycroftAI/mimic-recording-studio
* https://voice.mozilla.org/
* https://github.com/mozilla/TTS
* https://raw.githubusercontent.com/mozilla/voice-web/master/server/data/de/sentence-collector.txt
* https://github.com/gras64/corpus-file-gen