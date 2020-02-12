import tkinter as tk
import cv2
import numpy as np
from tkinter import messagebox

def textToSign():    
    a = entry1.get()
    a = a.lower()
    a=a.split()
    for i in a:
        if i in (l):
            b=".png"
            c=i+b
            img=cv2.imread(c)
            cv2.putText(img, i, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (200,80,0,255),3)
            cv2.imshow(i, cv2.resize(img,(300,300)))
            cv2.waitKey(3000)
            cv2.destroyAllWindows()  
        elif i in ('a', 'an', 'the', 'is', 'are', 'am'):
            messagebox.showinfo("Grammar Word", "Sign not found for \""+i+"\"")
        else:
            j=list(i)
            for letter in j:
                e="letter_"
                f=".JPG"
                g=e+letter+f
                img2=cv2.imread(g)
                cv2.namedWindow('image', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('image', 300,300)
                cv2.putText(img2, letter, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (100,80,0,255),3)
                cv2.imshow(i, cv2.resize(img2,(300,300)))
                cv2.waitKey(3000)
                cv2.destroyAllWindows()    

l = ['aboard', 'baby', 'beside','book', 'bowl', 'bridge', 'camp', 'cartridge', 'eight', 'five', 'fond', 'four', 'friend', 'glove',
     'hang', 'high', 'house', 'I', 'i', 'me', 'man', 'marry', 'meat', 'medal', 'midday', 'middle', 'money', 'moon','mother', 'nine',
     'one', 'opposite', 'prisoner','ring', 'rose', 'see', 'seven', 'short', 'six', 'superior','ten','thick','thin', 'three','tobacco',
     'two', 'up', 'watch', 'write', 'you', 'hi', 'good','morning', 'afternoon', 'night', 'what', 'where', 'how']
position = (10,190)
    
top= tk.Tk()

canvas1 = tk.Canvas(top, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(top, text='Type below')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

entry1 = tk.Entry (top) 
canvas1.create_window(200, 140, window=entry1)

button1 = tk.Button(text='Find Images', command=textToSign, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

top.mainloop()
