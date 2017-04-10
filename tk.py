"""
Project: A Tkinter App which will act as a media center and can be controlled using an IR remote

A project by:
-Manash Jyoti Deka
-Ankith Kumar
-Apoorv Kushal
-Arjun Rajeev
-Abijith Choutagunta
"""
#GUI CODE
import tkinter as tk                    #For class root(tk.Tk)
from tkinter import *                   #Label Nad Other Widgets
import os                               #For Os.Startfile and listdir
import subprocess                       # for Double Click Function
from PIL import Image, ImageTk          #for importing image

def get_filenamesaudio():
    path = r"D://Entertaintment/Songs/Revealed"
    return os.listdir(path)

def get_filenamesvideo():
    path = r"D://Entertaintment/Videos"
    return os.listdir(path)                                               #names of all files inside the folder


class root(tk.Tk):
    def __init__(self,*args,**kwargs):                                    #args for passing multiple arguements and kwargs for named arguements
        tk.Tk.__init__(self,*args,**kwargs)                               #initialise tkinter
        container = tk.Frame(self)                                        #container contains all the frames
        container.pack(side="top", fill="both", expand="True")            #for packing the container in the frame
        container.grid_rowconfigure(0, weight=1)                          #part of tkinter.tk (size, priority)
        container.grid_columnconfigure(0, weight=1)                       #(size=minimum, priority = high)

        self.frames = {}                                                  #dictionary for the 3 frames we have used

        for F in (StartPage, PageOne, PageTwo):                           #names of the three frames
            frame = F(container,self)                                     #frames F in the container
            self.frames[F] = frame                                        #whichever frame that is to be shown
            frame.grid(row = 0, column = 0, sticky="nsew")                #grid arrangement starting from row=0 column=0
                                                                          #sticky=nsew=north south east west
        self.show_frame(StartPage)                                        #what frame is to be shown at first

    def show_frame(self,cont):                                            #function to show the frame
        frame = self.frames[cont]
        frame.tkraise()                                                   #raise the frame to the front


class StartPage(tk.Frame):                                   #first frame i.e., the start page and inherit from tk.frame
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)                       #parent clasx is the class root


        self.image = Image.open("D://Study/Moodle/Semester 7/python/kill/backgrou.png")    #openning the image
        self.img_copy= self.image.copy()                                                #copying the imageto img_copy
                                                                    #the image is copied for resizing it later on

        self.background_image = ImageTk.PhotoImage(self.image)      #setting it the background image

        self.background = Label(self, image=self.background_image)   #setting the background image as a label
        self.background.place(x=0, y=0, relwidth=1, relheight=1)     #from (x,y) = (0,0) with max height and width
        self.background.bind('<Configure>', self._resize_image)      #for resizing the background image

        label = tk.Label(self, text="Menu", font= ('times', 20, 'bold'), bg='cornflower blue')
        label.pack(pady=10,padx=10)                                   #Pack with gap of 10 units both in x and y axis

        #adding buttons
        button1= tk.Button(self, text="Audios", command=lambda: controller.show_frame(PageOne),fg="white",bg="gray24")  #takes you tyo the "PageOne"
        button1.pack(pady=60)                                           #Pack the button with 60 units gap from the previous item "label"
        button1.config(width=23, height=5)                              #Button Width and height
        button1.config(highlightbackground="OliveDrab2")
        button1.config(highlightcolor="Red")
        button1.focus_set()                                             #set focus initially on the first button
        #adding button 2
        button2= tk.Button(self, text="Videos", command=lambda: controller.show_frame(PageTwo),fg="white",bg="gray24")
        button2.pack(pady =70)
        button2.config(width=23, height=5)



    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg='gray24')
        label = tk.Label(self, text="Audios", font= ('times', 22))
        label.config(fg = 'white', bg = 'gray24')
        label.pack(pady=10,padx=10)
        button3= tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button3.pack()
        button3.config(width=10, height=2)
        button3.focus_set()
        lb = tk.Listbox(self)
        lb.config(bg='White')
        for filename in get_filenamesaudio():
            if filename.endswith('.mp3'):
                lb.insert("end", filename)
        lb.bind("<space>", self.doubleclick)
        lb.pack(side="top", fill="both", expand=True)
        lb.config(takefocus=1)
        lb.selection_set(0)
        lb.activate(0)
        lb.see(0)
        self.image = Image.open("D://Study/Moodle/Semester 7/python/kill/music.png")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    def doubleclick(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print(value)
        ster = "D://Entertaintment/Songs/Revealed/"+value
        os.startfile(ster)

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg='gray24')
        label = tk.Label(self, text="Videos", font= ('times', 22))
        label.config(fg = 'white', bg = 'gray24')
        label.pack(pady=10,padx=10)
        button1= tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.focus_set()
        #list of items
        #tk.Tk.__init__(self, *args, **kwargs)
        lb = tk.Listbox(self)
        for filename in get_filenamesvideo():
            if filename.endswith('.mp4'):
                lb.insert("end", filename)
        lb.bind("<space>", self.doubleclick)
        lb.pack(side="top", fill="both", expand=True)
        lb.activate(0)
        self.image = Image.open("D://Study/Moodle/Semester 7/python/kill/video.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    def doubleclick(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print(value)
        ster = "D://Entertaintment/Videos/"+value
        os.startfile(ster)



app = root()
app.geometry("600x600")
app.wm_title("Mediafy")
app.iconbitmap(default='D://Study/Moodle/Semester 7/python/kill/drop.ico')
app.mainloop()
