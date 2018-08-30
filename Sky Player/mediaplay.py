import os

import pygame

from tkinter.filedialog import askdirectory

from tkinter import *

root=Tk()

root.minsize(500,500)

root.title("Sky Music Player")

playlistofsongs= []
count=0
index=0
ctr=9

def nextsong(event):
	global index
	if(index==(len(playlistofsongs)-1)):
		index=0
	else:	
		index=index+1
	pygame.mixer.music.load(playlistofsongs[index])
	pygame.mixer.music.play()

def prevsong(event):
	global index
	if(index==0):
		index=len(playlistofsongs)-1
	else:	
		index=index-1
	
	pygame.mixer.music.load(playlistofsongs[index])
	pygame.mixer.music.play()
	
def pausesong(event):
	pygame.mixer.music.pause()

def unpausesong(event):
	pygame.mixer.music.unpause()

def stopsong(event):
	pygame.mixer.music.stop()	
	
def increasevol(event):
	global ctr
	ctr=ctr+1
	if(ctr<=10 and ctr>=0):
		
		ctr=ctr/10
		print(ctr*10)
		pygame.mixer.music.set_volume(ctr)
		ctr=ctr*10

def decreasevol(event):
	global ctr
	ctr=ctr-1
	if(ctr>=0 and ctr<=10):
		ctr=ctr/10
		print(ctr*10)
		pygame.mixer.music.set_volume(ctr)
		ctr=ctr*10	
	
def dirchooser():
        directory=askdirectory()
        os.chdir(directory)

        for files in os.listdir(directory):
                if(files.endswith(".mp3") or files.endswith(".ogg") or files.endswith(".wav")):
                        playlistofsongs.append(files)
                        print(files)
                else:
                        print("no music file in dir")
                 	
def startplayingfromplaylist(event):                 	
        pygame.mixer.init()
        pygame.mixer.music.load(playlistofsongs[0])
        pygame.mixer.music.play()


	

def appearlist(event):
	global count
	if(count==0):	
		listbox=Listbox(root,width=50, height=15)
		listbox.pack()
		playlistofsongs.reverse()
		for items in playlistofsongs:
			listbox.insert(0,items)
		playlistofsongs.reverse()
		count=count+1

def buttons():
	
	listdisplaybutton=Button(root,text='Display Playlist V')
	listdisplaybutton.pack()
	listdisplaybutton.bind("<Button-1>",appearlist)	
	
	splaybutton=Button(root,text='Start Playing')
	splaybutton.pack()
	splaybutton.bind("<Button-1>",startplayingfromplaylist)
	
	nextbutton=Button(root,text='Next Song')
	nextbutton.pack()
	nextbutton.bind("<Button-1>",nextsong)

	pausebutton=Button(root,text='Pause')
	pausebutton.pack()
	pausebutton.bind("<Button-1>",pausesong)
	
	unpausebutton=Button(root,text='Unpause')
	unpausebutton.pack()
	unpausebutton.bind("<Button-1>",unpausesong)
	
	prevbutton=Button(root,text='Previous Song')
	prevbutton.pack()
	prevbutton.bind("<Button-1>",prevsong)

	stopbutton=Button(root,text='Stop')
	stopbutton.pack()	
	stopbutton.bind("<Button-1>",stopsong)
	
	
	
	volumebutton1=Button(root,text='Volume Up +')
	volumebutton1.pack()
	volumebutton1.bind("<Button-1>",increasevol)
	
	volumebutton2=Button(root,text='Volume Down -')
	volumebutton2.pack()
	volumebutton2.bind("<Button-1>",decreasevol)
	
###############################################################################

dirchooser()

label=Label(root,text='Sky Player')
label.pack()
		
buttons()		#displaying buttons

root.mainloop()		#mainloop of tkinter window

