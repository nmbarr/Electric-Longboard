#Test script to make a GUI

import tkinter as tk
from tkinter import filedialog, Text
import os

#Initialize window
root = tk.Tk()
root.title("GUI Test")

#Navigate to apps
def add_app():
    filename= filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(("executables", "*.exe"), ("all files", "*.*")))

#Change window size, BG color
canvas = tk.Canvas(root, height=320, width=480, bg="#263D42")
canvas.pack()

#Create Container for widgets
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Create button on root
open_file = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=add_app)
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=add_app)
run_apps.pack()

#Create window
root.mainloop()
