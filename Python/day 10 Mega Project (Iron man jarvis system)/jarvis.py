import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import pywhatkit

# Logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format=" [ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# Activating Voice
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 190)
voices = engine.getProperty("voices")

# Set voice to Microsoft David (male)
for v in voices:
    if "David" in v.name:
        engine.setProperty('voice', v.id)
        break


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    """Recognize voice command"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return "none"

    return query


def greeting():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning sir! How are you doing?")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")


def play_music():
    music_dir = r"C:\Inception BD\Data-Science-with-Generative-AI\Python\day 10 Mega Project (Iron man jarvis system)\Music"

    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))
        else:
            speak("No music files found in your music directory.")
    except Exception:
        speak("Sorry sir, I could not find your music folder.")


# Start
greeting()
speak("I am tamimystic. Please tell me how may I help you today?")

while True:
    querys = takeCommand()

    if querys == "none":
        continue

    querys = querys.lower()
    print(querys)

    if "your name" in querys:
        speak("My name is Jarvis")
        logging.info("User asked for assistant's name.")

    elif "time" in querys:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")

    elif "open google" in querys:
        speak("What should I search on Google?")
        search = takeCommand().lower()
        if search != "none":
            webbrowser.open(f"https://www.google.com/search?q={search}")
            speak(f"Searching Google for {search}")
        else:
            speak("Sorry sir, I could not understand the search keyword.")

    elif "open calculator" in querys:
        speak("Opening calculator")
        subprocess.Popen("calc.exe")

    elif "wikipedia" in querys:
        speak("Searching Wikipedia...")
        querys = querys.replace("wikipedia", "")

        try:
            results = wikipedia.summary(querys, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("Sorry sir, I could not find anything on Wikipedia.")

    elif "play on youtube" in querys:
        song = querys.replace("play on youtube", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "music" in querys:
        speak("Ok sir, playing music")
        play_music()

    elif "exit" in querys:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()

    else:
        speak("I can not understand.")
