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
    con = sqlite3.connect("_isim__.db")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS names(ad TEXT)")

    con.commit()
    cursor.execute("select * from names")
    name = cursor.fetchall()
    if(len(name)==0):
        speak("Merhaba ben sesli asistan sana nasıl hitap etmemi istersin")
        print("Merhaba ben sesli asistan sana nasıl hitap etmemi istersin")

        response=sr.Recognizer()
        with sr.Microphone() as source:
            audio=response.listen(source)
        try:
            pharse = response.recognize_google(audio, language="tr-TR")
            phrase = pharse.lower()
            print(phrase)
        except sr.UnknownValueError:
            speak("üzgünüm anlayamadım lütfen tekrar et")
            print("Asistan:Üzgünüm anlayamadım,lütfen tekrar et")


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
        speak("günaydın {}".format(isim))
        print("Asistan:Günaydın {}".format(isim))
    elif (hour >= 12 and hour < 18):
        speak("iyi öğlenler {}".format(isim))
        print("Asistan:İyi öğlenler {}".format(isim))
    elif (hour >= 18 and hour < 22):
        speak("iyi akşamlar {}".format(isim))
        print("Asistan:İyi akaşamlar{}".format(isim))
    else:
        speak("iyi geceler {}".format(isim))
        print("Asistan:İyi geceler {}".format(isim))


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
            speak("anlayamadım")
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            speak("sistem çalışmıyor")
            print("Asistan: Sistem çalışmıyor")
        return voice

def response(voice):
    if "nasılsın" in voice:
        temp1=["iyiyim teşekkür ederim.","sana yardımcı olabilğim sürece iyiyim"]
        temp1=random.choice(temp1)
        speak(temp1)
        print("Asistan:{}".format(temp1))
    if "kaç yaşındasın sen" in voice or "yaşın kaç" in voice or "kaç yaşındasın" in voice:
        speak("seninle aynı yaştayım")
        print("Asistan:Seninle aynı yaştayım")
    if "merhaba" in voice:
        speak("sana da merhaba")
        print("Asistan:Sana da merhaba")
    if "selam" in voice:
        speak("sana da selam olsun")
        print("Asistan:Sana da selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
        print("Asistan:Rica ederim")
    if "görüşürüz" in voice:
        speak("görüşürüz")
        print("Asistan:görüşürüz")
        exit()
    if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice:
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
        print(today)


    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)
        print(selection + clock)


    if "google'da ara" in voice:
        speak("ne aramamı istersin")
        print("Asistan:Ne aramamı istersin")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))

    if "bugün hava nasıl" in voice or "hava durumu nasıl" in voice or "hava nasıl" in voice:
        url_="https://www.google.com/search?q=hava+durumu"
        webbrowser.get().open(url_)
        speak("hava durumu için bulabildklerim açıyorum.")



def special_day():
    an=datetime.now()
    if an.month==4:
        if an.day==23:
            speak("23 nisan ulusal egemenlik ve çocuk bayramı kutlu olsun")
            print("23 nisan ulusal egemenlik ve çocuk bayramı kutlu olsun")
    elif an.month==5:
        if an.day==19:
            speak("19 mayıs gençlik ve atatürkü anma bayramı kutlu olsun")
            print("19 mayıs gençlik ve atatürkü anma bayramı kutlu olsun")
    elif an.month==10:
        if an.day==29:
            speak("29 ekim cumhuriyet bayramı kutlu olsun")
            print("29 ekim cumhuriyet bayramı kutlu olsun")
    elif an.month==8:
        if an.day==30:
            speak("30 ağustos zafer bayramı kutlu olsun")
            print("30 ağustos zafer bayramı kutlu olsun")

get_name()
special_day()
speak("Sana nasıl yardımcı olmamı istersin")
print("Sana nasıl yardımcı olmamı istersin")
while True:
 voice = record()
 if voice != " ":
     voice = voice.lower()
     print(voice)
     response(voice)
