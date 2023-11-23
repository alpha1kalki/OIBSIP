# Create a Voice Assistant

import openai 
import pyttsx3
import speech_recognition as sr
import time
#import pyaudio

# Ser your OpenAI API 

openai.api_key = "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"

# Initialize the text to speech engine

engine = pyttsx3.init()

def trancribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        Audio = recognizer.record(source)
    try:
        return recognizer.recognize_gooogle(openai.audio)
    except:
        print('Skipping Unknown error') 

def generate_response(prompt):
    response = openai.completion.create(


    engine = "text_davinci_003",
    prompt = prompt,
    max_tokens = 1000,
    n=1,
    stop = None,
    temperature = 0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("say 'Alpha' to start recording your questions...")
        with sr.Microphone()as source:
            recognizer = sr.Recognozer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower()=="Alpha":
                   # Record audio
                   filename = "input.wav"
                   print("say your question...")
                   with sr.Microphone() as Source:
                       recognizer = sr.Recognizer()
                       source.pause_threshold = 1
                       audio = recognizer.listen(source,phrase_time_limit = None,timeout = None)
                       with open (filename,"wb")as f:
                           f.write(audio.get_wav_data())
                           
                    # Transcribe recorded audio to text
                   text = trancribe_audio_to_text(filename)
                   if text:
                       print(f"You said: {text}")

                       #Generate response using GPT-3

                       response = generate_response(text)
                       print(f"GPT-3 says:{response}")

                       speak_text(response)

            except Exception as e:
                print("An error occured :{}".format(e))       

if __name__ == "__main__":
    main()

  


                 