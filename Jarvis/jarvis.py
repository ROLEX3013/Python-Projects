import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit  


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('language', 'hi')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning, Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, Sir")
    else:
        speak("Good evening, Sir")
    speak("I am Jarvis. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("Say that again, please.")
        return "None"
    return query

def play_youtube_song(song_name):
    try:
        speak(f"Playing {song_name} on YouTube")
        pywhatkit.playonyt(song_name)
    except Exception as e:
        speak("Sorry, I am unable to play that song at the moment.")
        print(e)

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'play music' in query:
            music_dir = "D:\\music"  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            speak("Playing music")

        elif 'play' in query and ('song' in query or 'youtube' in query):
            song_name = query.replace('play', '').replace('song', '').replace('youtube', '').strip()
            play_youtube_song(song_name)

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'quit' in query:
            speak("Thank you, Sir. See you soon!")
            exit()
