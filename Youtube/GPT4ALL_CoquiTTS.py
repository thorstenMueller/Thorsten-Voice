from pygpt4all.models.gpt4all_j import GPT4All_J
from TTS.api import TTS
import wave,sys,pyaudio

def new_text_callback(text):
    print(text, end="")

model = GPT4All_J('./ggml-gpt4all-j-v1.2-jazzy.bin')
outText = model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
print(outText)

tts = TTS(model_name="tts_models/en/ljspeech/vits--neon")
tts.tts_to_file(text=outText)

wf = wave.open('output.wav')
p = pyaudio.PyAudio()
chunk = 1024
stream = p.open(format=
    p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output = True
)
data = wf.readframes(chunk)
while data != '':
    stream.write(data)
    data=wf.readframes(chunk)
