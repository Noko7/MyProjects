from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil 


#functions
def select_path():
    #allows user to select the path from explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():    
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #download viedo
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move to selecter directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')

screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500, height=500, background='#4A4A4A')
canvas.pack()

#image logo 
logo_img = PhotoImage(file='ytimg.png')

#resiize logo
logo_img = logo_img.subsample(3, 3)
canvas.create_image(250, 70, image=logo_img)

#link field
link_field = Entry(screen, width=30, font=('Arial', 15))
link_label = Label(screen, text="Enter Download Link:", font=('Arial', 15), pady='5', padx='22', fg='black')

#Select path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15), fg='black')
select_btn =  Button(screen, text="Select Path", bg='grey', padx='22', pady='5',font=('Arial', 15), fg='black', command=select_path)

#add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Addd widget to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#downlad buttons
download_btn = Button(screen, text="Download File",bg='grey', padx='22', pady='5',font=('Arial', 15), fg='black', command=download_file)

#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop() 