# This script generates the folder structure for ljspeech-1.1 processing from mimic-recording-studio database

# Changelog
# v1.0  - Initial release by Thorsten Müller (https://github.com/thorstenMueller/deep-learning-german-tts)
# v1.1  - Great improvements by Peter Schmalfeldt (https://github.com/manifestinteractive)
#           - Audio processing with ffmpeg (mono and samplerate of 22.050 Hz)
#           - Much better Python coding than my original version
#           - Greater logging output to command line
#           - See more details here: https://gist.github.com/manifestinteractive/6fd9be62d0ede934d4e1171e5e751aba
#           - Thanks Peter, it's a great contribution :-)
# v1.2  - Added choice for choosing which recording session should be exported as LJSpeech
# v1.3  - Added parameter mrs_dir to pass directory of Mimic-Recording-Studio
# v1.4  - Script won't crash when audio recorded has been deleted on disk
# v1.5  - Added parameter "ffmpeg" to make converting with ffmpeg optional

from genericpath import exists
import glob
import sqlite3
import os
import argparse
import sys

from shutil import copyfile
from shutil import rmtree

# Setup Directory Data
cwd = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(cwd, "dataset")
output_dir_audio = ""
output_dir_audio_temp=""
output_dir_speech = ""

# Create folders needed for ljspeech
def create_folders():
  global output_dir
  global output_dir_audio
  global output_dir_audio_temp
  global output_dir_speech

  print('→ Creating Dataset Folders')

  output_dir_speech = os.path.join(output_dir, "LJSpeech-1.1")

  # Delete existing folder if exists for clean run
  if os.path.exists(output_dir_speech):
    rmtree(output_dir_speech)

  output_dir_audio = os.path.join(output_dir_speech, "wavs")
  output_dir_audio_temp = os.path.join(output_dir_speech, "temp")

  # Create Clean Folders
  os.makedirs(output_dir_speech)
  os.makedirs(output_dir_audio)
  os.makedirs(output_dir_audio_temp)

def convert_audio():
  global output_dir_audio
  global output_dir_audio_temp

  recordings = len([name for name in os.listdir(output_dir_audio_temp) if os.path.isfile(os.path.join(output_dir_audio_temp,name))])
  
  print('→ Converting %s Audio Files to 22050 Hz, 16 Bit, Mono\n' % "{:,}".format(recordings))

  # Please use `pip install ffmpeg-python`
  import ffmpeg

  for idx, wav in enumerate(glob.glob(os.path.join(output_dir_audio_temp, "*.wav"))):

    percent = (idx + 1) / recordings

    print('› \033[96m%s\033[0m \033[2m%s / %s (%s)\033[0m ' % (os.path.basename(wav), "{:,}".format((idx + 1)), "{:,}".format(recordings), "{:.0%}".format(percent)))

    # Convert WAV file to required format
    (ffmpeg
      .input(wav)
      .output(os.path.join(output_dir_audio, os.path.basename(wav)), acodec='pcm_s16le', ac=1, ar=22050, loglevel='error')
      .overwrite_output()
      .run(capture_stdout=True)
    )


def copy_audio():
  global output_dir_audio

  print('→ Using ffmpeg to convert recordings')
  recordings = len([name for name in os.listdir(output_dir_audio_temp) if os.path.isfile(os.path.join(output_dir_audio_temp,name))])
  
  print('→ Copy %s Audio Files to LJSpeech Dataset\n' % "{:,}".format(recordings))

  for idx, wav in enumerate(glob.glob(os.path.join(output_dir_audio_temp, "*.wav"))):    
    copyfile(wav,os.path.join(output_dir_audio, os.path.basename(wav)))

def create_meta_data(mrs_dir):
  print('→ Creating META Data')

  conn = sqlite3.connect(os.path.join(mrs_dir, "backend", "db", "mimicstudio.db"))
  c = conn.cursor()

  # Create metadata.csv for ljspeech
  metadata = open(os.path.join(output_dir_speech, "metadata.csv"), mode="w", encoding="utf8")

  # List available recording sessions
  user_models = c.execute('SELECT uuid, user_name from usermodel ORDER BY created_date DESC').fetchall()
  user_id = user_models[0][0]

  for row in user_models:
    print(row[0] + ' -> ' + row[1])

  user_answer = input('Please choose ID of recording session to export (default is newest session) [' + user_id + ']: ')

  if user_answer:
    user_id = user_answer


  for row in c.execute('SELECT audio_id, prompt, lower(prompt) FROM audiomodel WHERE user_id = "' + user_id + '" ORDER BY length(prompt)'):
    source_file = os.path.join(mrs_dir, "backend", "audio_files", user_id, row[0] + ".wav")
    if exists(source_file):
      metadata.write(row[0] + "|" + row[1] + "|" + row[2] + "\n")
      copyfile(source_file, os.path.join(output_dir_audio_temp, row[0] + ".wav"))
    else:
      print("Wave file {} not found.".format(source_file))

  metadata.close()
  conn.close()

def cleanup():
  global output_dir_audio_temp

  # Remove Temp Folder
  rmtree(output_dir_audio_temp)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--mrs_dir', required=True)
  parser.add_argument('--ffmpeg', required=False, default=False)
  args = parser.parse_args()
  
  if not os.path.isdir(os.path.join(args.mrs_dir,"backend")):
    sys.exit("Passed directory is no valid Mimic-Recording-Studio main directory!")

  print('\n\033[48;5;22m  MRS to LJ Speech Processor  \033[0m\n')

  create_folders()
  create_meta_data(args.mrs_dir)

  if(args.ffmpeg):
    convert_audio()
  
  else:
    copy_audio()
  
  cleanup()

  print('\n\033[38;5;86;1m✔\033[0m COMPLETE【ツ】\n')

if __name__ == '__main__':
  main()
