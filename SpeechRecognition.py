//install pydub and SpeechRecognition package
import speech_recognition as sr
from pydub import AudioSegment
import os

# List of OGG audio file names
ogg_files = ["t0.ogg","t1.ogg","t2.ogg","t3.ogg","t4.ogg","t5.ogg","t6.ogg","t7.ogg","t8.ogg","t9.ogg","t10.ogg","t11.ogg","t12.ogg","t13.ogg","t14.ogg","t15.ogg","t16.ogg","t17.ogg","t18.ogg","t19.ogg","t20.ogg","t21.ogg","t22.ogg","t23.ogg","t24.ogg","t25.ogg","t26.ogg","t27.ogg","t28.ogg","t29.ogg","t30.ogg",]  

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
wav_files = [t0.wav","t1.wav","t2.wav","t3.wav","t4.wav","t5.wav","t6.wav","t7.wav","t8.wav","t9.wav","t10.wav","t11.wav","t12.wav","t13.wav","t14.wav","t15.wav","t16.wav","t17.wav","t18.wav","t19.wav","t20.wav","t21.wav","t22.wav","t23.wav","t24.wav","t25.wav","t26.wav","t27.wav","t28.wav","t29.wav","t30.wav"]
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





import pandas as pd

# List of transcribed text
transcribed_text = ["Transcribed text 1", "Transcribed text 2", "Transcribed text 3","Transcribed text 4"]  # Replace with your transcribed text

# Create a DataFrame
df = pd.DataFrame({'Transcribed Text': transcribed_text})

# Save the DataFrame to a CSV file
df.to_csv('transcribed_text.csv', index=False)


