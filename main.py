from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import webbrowser



def response(voice):
    if "merhaba" in voice:
        speak("merhaba")
        print("merhaba")
    if "selam" in voice:
        speak("selam naberr ")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim ")
    if "görüşürüz" in voice:
        speak("görüşürüz kendine çok iyi davran")
        exit()
    if "hangi gündeyiz" in voice:
        today=time.strftime("%A")
        today.capitalize()
        if today=="Sunday":
            today="Pazar"
        elif today=="Monday":
            today="Pazartesi"
        elif today=="Tuesday":
            today="Salı"
        elif today=="Wednesday":
            today="Çarşamba"
        elif today=="Thursday":
            today="Perşembe"
        elif today=="Friday":
            today="Cuma"
        elif today=="Saturday":
            today="Cumartesi"
        speak(today)
    if "saat kaç" in voice:
        selection=["Saat şu an:","Hemen bakıyorum:","Saat:"]
        clock=datetime.now().strftime("%H:%M")
        selection=random.choice(selection)
        speak(clock+selection)

r=sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")
        return voice


def speak(string):
    tts = gTTS(text=string, lang="tr")
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("merhaba")
while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        response(voice)