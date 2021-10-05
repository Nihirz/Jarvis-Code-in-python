from os import path, spawnl
from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening")

    speak("Hello, I am Jarvis sir, Please Tell me How may i Help you? ")

def takeCommand():
    # It takes microphone  input  from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n" )


    except Exception as e :
        # print(e)
        print("Say that again Please....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('youremail.com',to,content)
    server.close()

if __name__ == "__name__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
    # Logic For executing tasks based on query
        if 'wikipedia' in query:
            speak ("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,senteces=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs =  os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open sublime' in query:
            subPath = "C:\\Sublime Text\\sublime_text.exe"
            os.startfile(subPath)

        elif 'send email to yash' in query:
            try:
                speak("What should i say? ")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been send! ")
            except Exception as e:
                print(e)
                speak("Sorry Sir i am not able to send this email")