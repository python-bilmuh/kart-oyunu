from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import random
from random import choice
import time
from datetime import date, datetime
import webbrowser
import sqlite3

con=sqlite3.connect("isim.db")
cursor=con.cursor()
def get_name(name):
    cursor.execute("CREATE TABLE IF NOT EXISTS names(ad TEXT)")
    cursor.execute("INSERT INTO names VALUES('{}')".format(name))
    con.commit()
    con.close()
    speak("Merhaba {}".format(name))



r=sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice

def response(voice):
    if "nasılsın" in voice:
        temp1=["iyiyim teşekkür ederim.","sana yardımcı olabilğim sürece iyiyim"]
        temp1=random.choice(temp1)
        speak(temp1)
    if "kaç yaşındasın sen" in voice or "yaşın kaç" in voice or "kaç yaşındasın" in voice:
        speak("seninle aynı yaştayım")
    if "merhaba" in voice:
        speak("sana da merhaba genç")
    if "selam" in voice:
        speak("sana 2 kere selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice:
        speak("görüşürüz canım")
        exit()
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içi Google'da bulabildiklerimi listeliyorum.".format(search))



def greeting():
    hour = datetime.now().hour
    if (hour >= 7 and hour < 12):
        speak("Günaydın")
    elif (hour >= 12 and hour < 18):
        speak("İyi öğlenler" )
    elif (hour >= 18 and hour < 22):
        speak("İyi akşamlar")
    else:
        speak("İyi geceler")


def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



greeting()
speak("Sana nasıl hitap etmemi istersin")
name=record()
get_name(name)
while True:
    voice = record()
    if voice != " ":
        voice = voice.lower()
        print(voice)
        response(voice)

