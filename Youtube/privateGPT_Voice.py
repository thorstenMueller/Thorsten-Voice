# Script is originally taken from https://github.com/imartinez/privateGPT/blob/main/privateGPT.py
# and i've added some STT and TTS stuff.
# See full tutorial on my "Thorsten-Voice" Youtube channel: https://youtu.be/qBs85JNyY7I

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os
from constants import CHROMA_SETTINGS

import whisper
from TTS.api import TTS

##############################
# Whisper for local STT part #
##############################

model = whisper.load_model("base")
result = model.transcribe("input.wav")
query = result["text"]

##################################
# PrivateGPT for query documents #
##################################
load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
print("Model type: " + model_type)
model_path = os.environ.get('MODEL_PATH')
print("Model path: " + model_path)
model_n_ctx = os.environ.get('MODEL_N_CTX')
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', callbacks=None, verbose=False)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)

print("")
print(">> Asking my documents: " + query)
print("")

res = qa(query)
print("")

############################
# Coqui for local TTS part #
############################
os.environ["TOKENIZERS_PARALLELISM"] = "false"
tts = TTS(model_name="tts_models/en/ljspeech/vits--neon")
tts.tts_to_file(text=res['result'])
