#!/usr/bin/python
import sys
import os
import tkinter as tk
import pyperclip

from tkinter import *
from tkinter import constants,filedialog,messagebox,font 
import webbrowser
from PIL import ImageTk,Image,ImageDraw



imgname = "a.jpeg"
top=tk.Tk()
#top.configure(background="black")
top.title("Captcha breaking")
#top.geometry("1300x1300")
#top.resizable(width=False, height=False)



w = 500
h = 250
x = 0
y = 0
# use width x height + x_offset + y_offset (no spaces!)
top.geometry("%dx%d+%d+%d" % (w, h, x, y))
# use a colorful frame
frame = tk.Frame(top, bg='black')
frame.pack(fill='both', expand='yes')
tmppppp123 = ''

def browsefunc():
	global imgname
	imgname = filedialog.askopenfilename()
	pathlabel.config(text=imgname)
	loadImage()
pathlabel = Label()
#pathlabel.pack()


w = tk.Label(frame, text="Captcha letters", bg="black", fg="White",  font=("Arial",18))
w.place(x=10,y=10)
width = 100
height = 20

def loadImage(): 
    global imgname 
    img = Image.open(imgname)
    im2 = img.resize((width, height), Image.NEAREST)  
    filename = ImageTk.PhotoImage(im2)
    w=Canvas(top,height=50,width=900,bg="white")
    w.image = filename  # <--- keep reference of your image
    w.create_image(200,15,anchor='nw',image=filename)
    w.pack()
    cmd1 = 'rm -rf input_image/*'
    os.system(cmd1)
    cmd1 = 'cp '
    cmd1 += imgname
    cmd1 += ' input_image/'
    os.system(cmd1)


def loadImage1(): 
    img = Image.open('input_image1/tmp.png')
    im2 = img.resize((width, height), Image.NEAREST)  
    filename = ImageTk.PhotoImage(im2)
    w=Canvas(top,height=50,width=900,bg="white")
    w.image = filename  # <--- keep reference of your image
    w.create_image(200,15,anchor='nw',image=filename)
    w.pack()
    cmd1 = 'cp '
    cmd1 += imgname
    cmd1 += ' input_image1/'
    os.system(cmd1)

img = Image.open(imgname)
#w = Canvas(gui,height= 200,width= 300)
w.pack()


#RUNNING NEWSAMP
def run():
	newsamp.main(imgname)
	
#RUNNING TEST1
def run1():
	test1.main(imgname)

#RUNNING CNN
def cnn():
      os.system('python solve_captchas_with_model.py')
      captcha_text = pyperclip.paste()
      captcha_text = 'Captcha text is: ' + captcha_text
      label1["text"] = captcha_text



#RUNNING CNN
def fnforweb():
      import webbrowser
      a_website = "https://www.google.com/"
      # Open url in a new window of the default browser, if possible
      webbrowser.open_new(a_website)
      os.system('python captcha_browser.py')
      captcha_text = pyperclip.paste()
      loadImage1()
      captcha_text = 'Captcha text is: ' + captcha_text
      label1["text"] = captcha_text


#entry=Entry(top,bg="white")
browse=Button(top,text="browse from local",activebackground="yellow", width=15,command=browsefunc)
browseweb=Button(top,text="browse from web",activebackground="yellow", width=15,command=fnforweb)
cnn=Button(top,text="Result",activebackground="yellow",width=10,command=cnn)
label1=Label(top,textvariable='', width=50)


browse.pack(side =TOP)
browseweb.pack(side =TOP)
cnn.pack(side=BOTTOM)
label1.pack(side=BOTTOM)


top.mainloop()
