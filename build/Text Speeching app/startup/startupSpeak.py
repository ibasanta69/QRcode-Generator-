import pyttsx3
import win32con
import win32gui
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ! Basant Chaudhary ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ! Basant Chaudhary")
    elif hour>=21 and hour< 22:
        speak("Good Night Basant Chaudhary have You Nice Dream !")
    else:
        speak("Good Evening  ! Basant")

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
wishMe()