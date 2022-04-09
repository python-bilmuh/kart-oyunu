#sesli_aistan
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

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


def get_name():
    con = sqlite3.connect("isiml.db")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS names(ad TEXT)")

    con.commit()
    cursor.execute("select * from names")
    name = cursor.fetchall()
    if(len(name)==0):
        speak("Merhaba ben sesli asistan sana nasıl hitap etmemi istersin")
        response=sr.Recognizer()
        with sr.Microphone() as source:
            audio=response.listen(source)
        try:
            pharse=response.recognize_google(audio,language="tr-TR")
            phrase = pharse.lower()
            print(phrase)
        except sr.UnknownValueError:
            speak("Üzgünüm anlayamadım,lütfen tekrar et")

        name_ = phrase.split(" ")
        cursor.execute("INSERT INTO names VALUES(?)",(name_))
        con.commit()

        cursor.execute("select * from names")
        name = cursor.fetchall()
        name=name_
        greeting(name_)
    else:
        greeting(name)

def greeting(isim):
    hour = datetime.now().hour
    if (hour >= 7 and hour < 12):
        speak("Günaydın {}".format(isim))
    elif (hour >= 12 and hour < 18):
        speak("İyi öğlenler {}" .format(isim))
    elif (hour >= 18 and hour < 22):
        speak("İyi akşamlar {}".format(isim))
    else:
        speak("İyi geceler {}".format(isim))



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
            speak("Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
            speak("Sistem çalışmıyor")
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
        speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))



def special_day():
    an=datetime.now()
    if an.month==4:
        if an.day==23:
            speak("23 nisan ulusal egemenlik ve çocuk bayramı kutlu olsun")
    elif an.month==5:
        if an.day==19:
            speak("19 mayıs gençlik ve atatürkü anma bayramı kutlu olsun")
    elif an.month==10:
        if an.day==29:
            speak("29 ekim cumhuriyet bayramı kutlu olsun")
    elif an.month==8:
        if an.day==30:
            speak("30 ağustos zafer bayramı kutlu olsun")






get_name()
speak("Sana nasıl yardımcı olmamı istersin")
while True:

    voice = record()
    if voice != " ":
        voice = voice.lower()
        print(voice)
        response(voice)

