from os import system
import numpy as np
import speech_recognition as sr
import whisper
from playsound import playsound
import time

#aanpasbaar
model = whisper.load_model("base")                 # model groote/type
def detect_wake_word(transcript, wake_word="momo"): # wake woord
    return wake_word.lower() in transcript.lower()


# Functie om spraak op te nemen en te transcriberen met Whisper voor het detecteren van het wake word
def listen_for_wake_word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

while True:
    # Functie om spraak op te nemen en te transcriberen met Whisper voor het detecteren van het wake word
    def listen_for_wake_word():
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)  # calibreert ruis
            print("Luistert naar het wake word 'momo'...")

            while True:
                # Neem korte fragmenten op
                print("Opnemen van audiofragment...")
                audio = recognizer.listen(source, timeout=3)

                # Sla de audio op als een tijdelijke .wav-bestand
                with open("temp_audio.wav", "wb") as f:
                    f.write(audio.get_wav_data())

                # Gebruik Whisper om de audio te transcriberen
                print("Analyseren van audio met Whisper...")
                result = model.transcribe("temp_audio.wav", language="nl")  # Specificeer Nederlands
                transcript = result['text']
                print(f"Opgevangen tekst: {transcript}")

                # Controleer of het wake word in de transcriptie zit
                if detect_wake_word(transcript):
                    print("Wake word 'momo' herkend! Start volledige transcriptie...")
                    playsound('/path/to/audio/file/WakeWordSound.mp3') #!!!!!!! AANPASSEN
                    break  # Stop als het wake word is herkend
                    
    # Functie om langere spraak te transcriberen na wake word detectie
    def transcribe_speech():
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        with microphone as source:
            print("Opnemen voor volledige transcriptie...")

            # Neem de volledige audio op
            audio = recognizer.listen(source)

            # Sla de audio op als een tijdelijke .wav-bestand
            with open("temp_audio_full.wav", "wb") as f:
                f.write(audio.get_wav_data())
                playsound('/path/to/audio/file/done-soundeff.mp3')#!!!!!!! AANPASSEN

            # Gebruik Whisper om de langere audio te transcriberen
            result = model.transcribe("temp_audio_full.wav", language="nl")  # Specificeer Nederlands
            print("Volledige transcriptie voltooid:")
            print(result['text'])

    if __name__ == "__main__":
        listen_for_wake_word()  # Luister naar het wake word "momo"
        transcribe_speech()  # Transcribeer na herkenning van het wake word

