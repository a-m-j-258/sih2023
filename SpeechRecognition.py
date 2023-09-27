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

# Initialize the recognizer
recognizer = sr.Recognizer()

# List of WAV audio file names
wav_files = ["audiotest.wav", "audiotest1.wav", "audiotest2.wav"]  # Add more file names as needed

# Create a folder to store the transcriptions
if not os.path.exists('transcriptions'):
    os.mkdir('transcriptions')

# Initialize a counter for naming the transcription files
file_counter = 1

# Loop through each WAV audio file and transcribe it
for wav_file in wav_files:
    try:
        # Load the WAV audio file
        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)  # Record the audio data

        # Recognize the speech
        text = recognizer.recognize_google(audio_data)

        # Write the transcription to a text file
        transcription_file = f'transcriptions/transcription{file_counter}.txt'
        with open(transcription_file, 'w') as transcribed_text:
            transcribed_text.write(f"Audio File: {wav_file}\n")
            transcribed_text.write(f"Transcribed Text: {text}\n")

        print(f"Transcription for {wav_file}:\n{text}\n")

        file_counter += 1
    except sr.UnknownValueError:
        print(f"Could not understand the audio in {wav_file}\n")
    except sr.RequestError as e:
        print(f"Could not request results for {wav_file}; {e}\n")

print("Transcription process completed.")

