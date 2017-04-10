"""
Project: A Tkinter App which will act as a media center and can be controlled using an IR remote

A project by:
-Manash Jyoti Deka
-Ankith Kumar
-Apoorv Kushal
-Arjun Rajeev
-Abijith Choutagunta
"""
#REMOTE control Code
import serial
from subprocess import check_output
import time
import os


port = "COM3"
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
nextbutton="0BF02FD\r\n"
previousbutton="0BF22DD\r\n"
up="0BFA05F\r\n"
down="0BFF00F\r\n"
closemedia="0BF926D\r\n"
select="0BFC23D\r\n"
closeapp="0BF12ED\r\n"
tex= ""
while True:
    l=[]
    out = ser.read()
    x=out.decode('ascii')
    text=""

    if(len(x)>0):
        tex+=str(x)
        while(len(x)!=0):
            out = ser.readline()
            x=out.decode('ascii')
            text+=str(x)
    time.sleep(0.1)
    l.append(text)
    tex=str(l[0])
    print(tex)

    if tex == '0BF02FD\r\n':
        print("Button Pressed:"+nextbutton)
        os.startfile("D://Study/Moodle/Semester 7/python/Final Project/tab.vbs")
    elif tex == previousbutton:
        print("Button Pressed:"+previousbutton)
        os.startfile("D://Study/Moodle/Semester 7/python/Final Project/shtab.vbs")
    elif tex == select:
        print("Button Pressed:"+select)
        os.startfile("D://Study/Moodle/Semester 7/python/Final Project/space.vbs")
    elif tex == up:
        print("Button Pressed:"+up)
        os.startfile("D://Study/Moodle/Semester 7/python/Final Project/up.vbs")
    elif tex == "":
        print("Waiting for input...")
    elif tex == down:
        print("Button Pressed:"+down)
        os.startfile("D://Study/Moodle/Semester 7/python/Final Project/down.vbs")
    elif tex == closemedia:
        try:
            check_output("Taskkill /IM Music.UI.exe /F", shell=True)
        except:
            pass

        try:
            check_output("Taskkill /IM Video.UI.exe /F", shell=True)
        except:
            pass
        try:
            check_output("Taskkill /IM wmplayer.exe /F", shell=True)
        except:
            pass
        try:
            check_output("Taskkill /IM vlc.exe /F", shell=True)
        except:
            pass
    elif tex == closeapp:
        check_output("Taskkill /IM python.exe /F", shell=True)
    else:
        print("Invalid Button")
