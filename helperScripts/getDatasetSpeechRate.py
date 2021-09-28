# This script gets speech rate per audio recording from a voice dataset (ljspeech file and directory structure)
# Writte by Thorsten Müller (deep-learning-german@gmx.net) and provided without any warranty.
# https://github.com/thorstenMueller/deep-learning-german-tts/
# https://twitter.com/ThorstenVoice

# Changelog:
# v0.1 - 26.09.2021 - Initial version

import os
import librosa
import csv

dataset_dir = "/Users/thorsten/Downloads/thorsten-export-20210909/" # Directory where metadata.csv is in
out_csv_file = os.path.join(dataset_dir,"speech_rate_report.csv")
decimal_use_comma = True # False: Splitting decimal value with a dot (.); True: Comma (,)

out_csv = open(out_csv_file,"w")
out_csv.write("filename;audiolength_sec;number_chars;chars_per_sec;remove_from_dataset\n")

# Open metadata.csv file
with open(os.path.join(dataset_dir,"metadata.csv")) as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        wav_file = os.path.join(dataset_dir,"wavs",row[0] + ".wav")

        # Gather values for report.csv output
        phrase_len = len(row[1]) - 1 # Do not count punctuation marks.
        duration = round(librosa.get_duration(filename=wav_file),2)
        char_per_sec = round(phrase_len / duration,2)

        if decimal_use_comma:
            duration = str(duration).replace(".",",")
            char_per_sec = str(char_per_sec).replace(".",",")

        out_csv.write(row[0] + ".wav;" + str(duration) + ";" + str(phrase_len) + ";" + str(char_per_sec) + ";no\n")

out_csv.close()
