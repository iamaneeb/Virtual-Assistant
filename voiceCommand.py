import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#voices[1] is female voice
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def callme():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour<=12:
        print("Good Morning Aneeb")
        speak("Good Morning Aneeb")
    elif hour >=12 and hour <18:
        print("Good Afternoon Aneeb")
        speak("Good Afternoon Aneeb")
    else:
        print("Good Evening Aneeb")
        speak("Good Evening Aneeb")
    speak("how can i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        speak("Are you saying anything, Because I dont get what you're saying,  Can you repeat that again")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('',to,content)
    server.close()




callme()
while True:
    query = takecommand().lower()

    if 'open wikipedia' in query:
        speak('Searching wikipedia....')
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(result)
        speak(result)

    elif 'open notepad' in query:
        path = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(path)

    elif 'open paint' in query:
        path = "C:\\Windows\\system32\\mspaint.exe"
        os.startfile(path)
    
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')

    elif 'thank you' in query:
        speak("your welcome, I am happy to help you")
        

    elif 'what is the time right now' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the current time is {strtime}")

    elif 'send a email to my friend' in query:
        try:
            speak("what do you want to send")
            content = takecommand()
            to = ""
            sendEmail(to,content)
            speak("your email has succesfully sented")
        except Exception as e:
            print(e)
            speak("iam unable to sent the email")
    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'stop the program' in query:
        print("Exiting...")
        speak("Exiting...")
        break
 