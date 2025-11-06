import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For speech recognition
import datetime  # For time and date
import webbrowser  # For web searches and opening sites

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Alexa. Please tell me how may I help you")

def takeCommand():
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
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'hello' in query:
            speak("Hello! How can I help you?")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {strDate}")

        elif 'search for' in query:
            search_query = query.replace("search for", "").strip()
            if search_query:
                speak(f"Searching the web for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                speak("Please specify what to search for.")

        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif 'open firefox' in query:
            speak("Opening Firefox.")
            import os
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")  

