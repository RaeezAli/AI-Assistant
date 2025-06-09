import pywhatkit
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser as web
import datetime
import re
import subprocess
import pyautogui
from time import sleep

enigne = pyttsx3.init('sapi5')
voices = enigne.getProperty('voices')
enigne.setProperty('voices', voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    enigne.say(audio)
    enigne.runAndWait()
    print(" ")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()

def GoogleSearch(query):
    replacements = ["jarvis", "what is", "search", "how to", "on", "google", "what do you mean by"]
    query = query.lower()
    for phrase in replacements:
        query = query.replace(phrase, "")
    query = re.sub(r'\s+', ' ', query).strip()

    if not query:
        Speak("Sorry, I didn't understand the query.")
        return

    pywhatkit.search(query)

    try:
        search = wikipedia.summary(query, 2)
        Speak(f": According To Your Search : {search}")
    except wikipedia.exceptions.PageError:
        Speak(": Sorry! The topic might not be on Wikipedia")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):
    time_now = query.replace("set alarm for ", "").replace("set ", "").replace("alarm ", "").replace("for ", "").replace(" and ", ":")
    Alarm_Time = str(time_now)
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == Alarm_Time:
            Speak("Wake Up Sir")
            pyautogui.alert(text='Alarm Time!', title='Alarm', button='OK')
            break
        elif current_time > Alarm_Time:
            break

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click, hotkey
    import pyperclip

    sleep(2)
    click(x=942, y=59)
    hotkey('ctrl', 'c')
    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('Downloads')

    Download(Link)
    Speak("Downloaded the video. You can check the Downloads folder.")

def SpeedTest():
    subprocess.run(["python", "SpeedTestGui.py"])

def wolframp(query):
    import wolframalpha
    api = "PUGTVE-UGAUTTV3L2"
    requester = wolframalpha.Client(api)
    requested = requester.query(query)
    try:
        ans = next(requested.results).text
        return ans
    except:
        Speak("Can't Fetch Details")

def calculator(query):
    term = query.replace("jarvis", "").replace("addition", "+").replace("subtraction", "-")
    term = term.replace("multiplication", "*").replace("division", "/")
    term = term.replace("add", "+").replace("sub", "-").replace("multiply", "*")
    term = term.replace("divided", "/").replace("plus", "+").replace("minus", "-")
    final = str(term)
    try:
        Speak(f"Your calculation answer is {wolframp(final)}")
    except:
        Speak("Can't Fetch Details")

def temp(query):
    term = query.replace("jarvis", "").replace("in", "").replace("what is", "").replace("temperature", "")
    final = term.strip()
    if 'outside' in final:
        var1  = 'Temperature in Karachi'
        Speak(f"{var1} is {wolframp(var1)}")
    else:
        var2 = "Temperature in " + final
        Speak(f"{var2} is {wolframp(var2)}")
