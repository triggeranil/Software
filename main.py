import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("1000x1000")
canvas.config(bg='black')

# Relative path to the directory you want to walk through
relative_path = "Video to Audio Converter/Audio/"


# Get the absolute path based on the current working directory
absolute_path = os.path.abspath(relative_path)
pattern = "*.mp3"

listBox = tk.Listbox(canvas, fg="cyan", bg="black", width =100, font=('poppins',14))
listBox.pack(padx=15,pady=15)

for root,dirs,files in os.walk(absolute_path):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)

canvas.mainloop()
#mainloop method is useful for taking user input and handling the GUI
