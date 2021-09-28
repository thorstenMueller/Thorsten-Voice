# This script removes recordings from an ljspeech file/directory structured dataset based on CSV file from "getDatasetSpeechRate"
# Writte by Thorsten Müller (deep-learning-german@gmx.net) and provided without any warranty.
# https://github.com/thorstenMueller/deep-learning-german-tts/
# https://twitter.com/ThorstenVoice

# Changelog:
# v0.1 - 26.09.2021 - Initial version

import os
import csv
import shutil

dataset_dir = "/Users/thorsten/Downloads/thorsten-export-20210909/" # Directory where metadata.csv is in
subfolder_removed = "___removed"
in_csv_file = os.path.join(dataset_dir,"speech_rate_report.csv")
to_remove = []

# Open metadata.csv file
with open(os.path.join(dataset_dir,in_csv_file)) as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row[4] == "yes":
            # Recording in that row should be removed from dataset
            to_remove.append(row[0])
            print("Recording " + row[0] + " will be removed from dataset.")

print("\n" + str(len(to_remove)) + " recordings has been marked for deletion.")

if len(to_remove) > 0:

    metadata_cleaned = open(os.path.join(dataset_dir,"metadata_cleaned.csv"),"w")

    # Create new subdirectory for removed wav files
    removed_dir = os.path.join(dataset_dir,subfolder_removed)
    if not os.path.exists(removed_dir):
        os.makedirs(removed_dir)

    # Remove lines from metadata.csv and move wav files to new subdirectory
    with open(os.path.join(dataset_dir,"metadata.csv")) as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            if (row[0] + ".wav") not in to_remove:
                metadata_cleaned.write(row[0] + "|" + row[1] + "|" + row[2] + "\n")
            else:
                # Move recording to new subfolder
                shutil.move(os.path.join(dataset_dir,"wavs",row[0] + ".wav"),removed_dir)
    
    metadata_cleaned.close()
