//install pydub and SpeechRecognition package
import speech_recognition as sr
from pydub import AudioSegment
import os

# List of OGG audio file names
ogg_files = ["audiotest.ogg", "audiotest1.ogg", "audiotest2.ogg","audiotest3.ogg"]  # Add more file names as needed

# Loop through each OGG file and convert to WAV
for ogg_file in ogg_files:
    # Load the OGG file
    ogg_audio = AudioSegment.from_file(ogg_file, format="ogg")

    # Generate a WAV file name based on the OGG file name
    wav_file = os.path.splitext(ogg_file)[0] + ".wav"

    # Export it as a WAV file
    ogg_audio.export(wav_file, format="wav")

    print(f"Converted {ogg_file} to {wav_file}")
