import win32con
import win32gui
import datetime
from tkinter import*
from tkinter.font import Font
from typing import Sized, TextIO
import pyttsx3
import os
from tkinter import Label
from tkinter import filedialog, messagebox
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning   !  ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Basant Sir Have you nice today")
    else:
        speak("Good Evening! Basant Sir Have you nice today")


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def text_to_speech():
    st1 = textentry.get("1.0", "end")
    speak(st1)


def clear_text_contents():
    textentry.delete('1.0', 'end')


def openfile():
    myfile = filedialog.askopenfilename(initialfile="")
    filing = open(myfile, 'r')
    # print(filing.read())
    textentry.insert('1.0', filing.read())


def savefile():
    svr = textentry.get('1.0', 'end')
    savefiles = filedialog.asksaveasfile(
        initialfile="untild.txt", title="File save", defaultextension='.txt', mode='w', filetypes=[('TXT', '*.txt')])
    try:
        savefiles.write(svr)
    except:
        print()
        # console hidde


the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)


textframe = Tk()
file = StringVar()
myfile = StringVar()
textframe.geometry("700x450")
textframe.resizable(False, False)
textframe.title("Text Speeching App")

textlabel = Label(textframe, text="Text To Speech",
                  font="Arial 15")
textlabel.place(x=290, y=15)

textentry = Text(textframe, width=70, height=20)
textentry.place(x=70, y=60)

textentry.place(x=70, y=60)
openfile = Button(textframe, text="Open ", width=8, command=openfile,
                  relief="groove", font="cursive 12")
openfile.place(x=5, y=100)


but1 = Button(textframe, text="Read", width=8,
              relief="groove", font="cursive 12", command=text_to_speech)
but1.place(x=5, y=150)


but2 = Button(textframe, text="Save", width=8, command=savefile,
              relief="groove", font="cursive 12")
but2.place(x=5, y=200)


but3 = Button(textframe, text="Clear", width=8, command=clear_text_contents,
              relief="groove", font="cursive 12")
but3.place(x=5, y=250)


but4 = Button(textframe, text="Exit", width=8,
              relief="groove", font="cursive 12", command=textframe.quit)
but4.place(x=5, y=300)


lababout = Label(textframe, text="Developed by Basanta chauhdary",
                 font="cursive 12").place(x=240, y=410)
wishMe()
textframe.mainloop()
