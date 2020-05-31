import tkinter as tk
from tkinter import filedialog,Text
import os


root = tk.Tk()
apps = []

#this saves the file in save.txt removing ','
if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps=f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        

#creating a fn to add apps in gui
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
                                          filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg="black",fg="white").pack()

def runApps():
    for app in apps:
        os.startfile(app)
#creating canvas
canvas = tk.Canvas(root,height=720,width=1280,bg="#006871").pack()

#creating a frame
frame = tk.Frame(root,bg="black")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

#creating buttons
openFile=tk.Button(canvas,text="Open File",padx=10,pady=5,fg="white",bg="#006871",command = addApp)
openFile.pack()
runApps=tk.Button(canvas,text="Run File",padx=10,pady=5,fg="white",bg="#006871",command = runApps)
runApps.pack()

#this runs the saved apps and loads it on label
for app in apps:
    label = tk.Label(frame,text=app,bg="black",fg="white").pack()

root.mainloop()

#this saves the apps in text file
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')