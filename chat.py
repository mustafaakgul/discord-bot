from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            #speak(ask)
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='en-US')
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

def speak(text):
    tts = gTTS(text=text, lang='en')
    file = 'voice.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def response(voice):
    if 'hi' in voice:
        speak('Hey you too')
    if 'whatsup' in voice:
        speak('Very well, thanks for asking')
    if 'batmobile' in voice:
        speak('I am the Batmobile')

speak("Me Batmobile")

while True:
    voice = record_audio()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)
    else:
        print("No voice")
