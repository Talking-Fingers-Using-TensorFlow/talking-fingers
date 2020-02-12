import tkinter as tk
import os

root = tk.Tk()

def ttsCallBack():
  os.system('python TextToSign.py')

A = tk.Button(root, text ="TextToSign", bg = "#b3d9ff", activebackground="#ccff99",
              bd=3, padx=7, pady=5, font="50", command =ttsCallBack)
B = tk.Button(root, text ="SignToText", bg = "#85a3e0", activebackground="#ccff99",
              bd=3, padx=7, pady=5, font="50")

A.grid(row=1, column=1, padx=25, pady=25)
B.grid(row=3, column=1,padx=25, pady=25)

root.mainloop()








