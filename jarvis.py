import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe ():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12:
        speak ("Good Morning Sir !")

    elif hour >=12 and hour <18:
        speak ("Good Afternoon Sir !")

    else :
        speak("Good Evening Sir")

    speak("I am somu's personal assistant , How may I help you ?")

def takeCommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . . ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing . . .  ")
        query =r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Please Say that Again...")
        return"None"
    return query


    
    
if __name__ == "__main__":

    
    wishMe()
    while True:
    
        query = takeCommand().lower()

        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak ("According to wikipedia")
            print(results)
            speak(results)

        

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

         

        elif 'music' in query:
            webbrowser.open("youtu.be/DYO_GLIWlRA?si=vp-uukBanZcRA5cm&t=28")

        elif 'song' in query:
            music_dir = 'C:\\Users\\user\\Music\\jarvis'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        # elif 'code' in query:
        #     codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codepath)

        elif 'lead code' in query:
            webbrowser.open("https://leetcode.com/")

        elif 'ok' in query:
            break;
    
                

        
