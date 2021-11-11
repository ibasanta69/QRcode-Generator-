from tkinter import *
from tkinter.font import BOLD
from tkinter import Label, Button
from PIL import Image, ImageTk
from tkinter import filedialog, Message
import qrcode


def fileopens():
    filepaths = filedialog.askopenfilename(
        initialfile="")

    filetext = open(filepaths, 'r')
    textfield.insert('1.0', filetext.read())


def cleartext():
    textfield.delete('1.0', 'end')


def savefile():
    saves = textfield.get('1.0', 'end')
    savefiles = filedialog.asksaveasfile(
        initialfile="untiled txt", defaultextension='.txt', mode='w', filetypes=[('TXT', '*.txt')])

    try:
        savefiles.write(saves)

    except:
        Message('unsuccessfully')


def qr(qrtxt):
    qrimage = qrcode.make(qrtxt)
    qrimage = qrimage.resize((200, 200), Image.ANTIALIAS)
    qrimage.save('qrcode.png')

    image = PhotoImage(file='qrcode.png')
    Qrfield.config(image=image)
    Qrfield.image = image  # to prevent garbage collection from deleting the image


def QRcodess():
    st1 = textfield.get('1.0', 'end')
    qr(st1)


window = Tk()
window.config(background='#b8cfc7')
window.title("QRcode Generator")
window.geometry("800x400")

qrimage=Image.open("qrcode.png")
qrim=qrimage.resize((200,200),Image.ANTIALIAS)
newqrimage=ImageTk.PhotoImage(qrim)

boxlabel = Label(text="Text Box", font=('Arial', 15, BOLD),
                 foreground='gray', background="#c1cee3")
boxlabel.place(x=240, y=6)

Qrlabel = Label(text="QRcode", font=('Arial', 15, BOLD),
                foreground='gray', background="#c1cee3")
Qrlabel.place(x=620, y=6)

Qrfield = Label(width=250, height=250, relief=GROOVE, image=newqrimage)
Qrfield.place(x=527, y=55)

textfield = Text(window, width=63, height=18, relief=GROOVE)
textfield.place(x=12, y=35)

openbutton = Button(text="Open", relief=GROOVE,
                    width=8, command=fileopens)
openbutton.place(x=97, y=340)

savebutton = Button(text="Save",
                    relief=GROOVE, width=8, command=savefile)
savebutton.place(x=185, y=340)

clearbutton = Button(text="Clear", command=cleartext,
                     relief=GROOVE, width=8)
clearbutton.place(x=280, y=340)

exitbutton = Button(text="Exit", relief=GROOVE,
                    width=8, command=window.quit)
exitbutton.place(x=377, y=340)

Createqrbutton = Button(text="Create QR", command=QRcodess,
                        relief=GROOVE, width=8)
Createqrbutton.place(x=580, y=340)


qrsavebutton = Button(text="Save QR",
                      relief=GROOVE, width=8)
qrsavebutton.place(x=675, y=340)

myself=Label(text="developed by basanta chaudhary",fg='black',font=('Arial',10,BOLD),background='#b8cfc7')
myself.place(x=177, y=373)
filepaths = StringVar()
window.mainloop()
