import sounddevice as sd
import numpy as np
import subprocess
import os
import wavio
import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator

# Configuration
RATE = 44100
DURATION = 5  # seconds
CHANNELS = 1
WAV_FILENAME = "temp_output.wav"
MP3_FILENAME = "output.mp3"
filename = "input.txt"

def record_and_save_audio():
    # Record audio
    print("Recording...")
    audio_data = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=CHANNELS, dtype=np.int16)
    sd.wait()  # Wait for recording to finish
    print("Recording finished.")

    # Save the audio data to a WAV file
    wavio.write(WAV_FILENAME, audio_data, RATE)

    # Convert WAV to MP3 using ffmpeg
    subprocess.run(["ffmpeg", "-y", "-i", WAV_FILENAME, MP3_FILENAME], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # Optional: remove the temporary WAV file
    os.remove(WAV_FILENAME)

def transcribe_from_mp3(filename):
    # Convert MP3 to WAV for transcription
    audio_segment = AudioSegment.from_mp3(filename)
    with sr.AudioFile(audio_segment.export(format="wav")) as source:
        recognizer = sr.Recognizer()
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)  # This uses Google Web Speech API
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='en').text
    return translated_text

if __name__ == "__main__":
    record_and_save_audio()
    transcription = transcribe_from_mp3(MP3_FILENAME)
    
    translated_text = translate_to_english(transcription)
    with open(filename, 'w') as file:
        file.write(translated_text)
