import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
import os
from mutagen.mp3 import MP3   #for length of song
import time
mixer.init()


class musicPlayer:
    def __init__(self, Tk):
        self.root = Tk
        self.root.title("GANNA LITE")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(background="grey")

        def openFile():
            global fileName
            fileName = filedialog.askopenfilename()
            

        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='Open', command=openFile)
        self.submenu.add_command(label='Exit', command=self.root.destroy)

        def about():
            tkinter.messagebox.showinfo('About Us', 'Music Player Created By SAIKAT')

        self.submenu2=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.submenu2)
        self.submenu2.add_command(label='About', command=about)



        # adding label--
        self.label1 = Label(text='GAANA LITE', bg="red", fg="red", font=22).place(x=50, y=20)
        self.label1 = Label(text="Lets Play It", bg="black", fg="white", font=20)
        self.label1.pack(side=BOTTOM, fill=X)


        def playmusic():
            try:
                paused
            except NameError:

                try:
                    mixer.music.load(fileName)
                    mixer.music.play()
                    self.label1['text']='Music_Playing...'
                    songinfo()
                    length_bar()
                    self.img1 = ImageTk.PhotoImage(file='musicBG3.jpg')
                    self.img2 = ImageTk.PhotoImage(file='musicBG1.jpg')
                    self.img3 = ImageTk.PhotoImage(file='musicBG9.jpg')
                    self.img4 = ImageTk.PhotoImage(file='musicBG5.jpg')
                    self.imgLabel = Label(self.root, text='', bg="white", bd=0)
                    self.imgLabel.place(x=50, y=60)
                    animation()
                except:
                    tkinter.messagebox.showerror("Error", "File could not found please try agian !")
            else:
                mixer.music.unpause()
                self.label1['text']='Music_Unpaused'
         # Animation--
        def animation():
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.img4
            self.img4=self.img1
            self.imgLabel.config(image=self.img1)
            self.imgLabel.after(3000, animation)

        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music_stopped'
        
        def pausemusic():
            global paused
            paused = TRUE
            mixer.music.pause()
            self.label1['text']='Music_paused'


        def volume(vol):
            volume = int(vol)/100
            mixer.music.set_volume(volume)

        def mute():
            self.scale.set(0)    
            self.mute=ImageTk.PhotoImage(file="muteI1.png")
            mute=Button(self.root, image=self.mute, bd=0, bg="grey", command=unmute).place(x=250, y=290)
            self.label1['text']='Music Mute'

        def unmute():
            self.scale.set(25)  
            self.volImg = ImageTk.PhotoImage(file="vol1.png")
            volImg = Button(self.root, image=self.volImg, bg='grey', bd=0 ,command=mute).place(x=250, y=290)  
            self.label1['text']='Music Unmute'

        def length_bar():
            curr_time=mixer.music.get_pos()/1000
            convert_curr_time = time.strftime('%M:%S', time.gmtime(curr_time))
            

            song_mute = MP3(fileName)  #for select MP3 songs
            song_mute_length = song_mute.info.length # for music file length  
            convert__song_mute_length = time.strftime('%M:%S', time.gmtime(song_mute_length))
            self.lengthbar.config(text=f'Total Duration:{convert_curr_time}  {convert__song_mute_length}')

            self.lengthbar.after(1000, length_bar)


        self.lengthbar=Label(self.root, text='Total Length:-00:00', bg='black', fg='white', font=20)
        self.lengthbar.place(x=5, y=270)

        self.filelabel=Label(text="Lets Rock -- Select And Play", bg='black', fg='white', font=22)
        self.filelabel.place(x=50, y=20)    

        def songinfo():
            self.filelabel['text']='Current Music : ' + os.path.basename(fileName)
         # Adding leftsideimgage
        # self.L_photo = ImageTk.PhotoImage(file="music2.jpg")
        # L_photo = Label(self.root, image=self.L_photo).place(x=240, y=80, width=500, height=250)

        # adding Images
        self.photo=ImageTk.PhotoImage(file='mainimg1.jpg')
        photo=Label(self.root, image=self.photo, bg="white", bd=0).place(x=50, y=60)

        self.ganna= ImageTk.PhotoImage(file='Ganna1.png')
        ganna=Label(self.root, image=self.ganna , bd=0).place(x=5, y=10)
        

        self.photo_b1 = ImageTk.PhotoImage(file="play6.png")
        photo_b1 = Button(self.root, image=self.photo_b1, bd=0, bg="grey", command=playmusic).place(x=5, y=300)

        self.photo_b2 = ImageTk.PhotoImage(file="pausebut1.png")
        photo_b2 = Button(self.root, image=self.photo_b2, bd=0, bg='grey', command=pausemusic).place(x=85, y=300)

        self.photo_b3 = ImageTk.PhotoImage(file="stop1111.png")
        photo_b3 = Button(self.root, image=self.photo_b3, bd=0, bg='grey', command=stopmusic).place(x=165, y=300)

        self.volImg = ImageTk.PhotoImage(file="vol1.png")
        volImg = Button(self.root, image=self.volImg, bg='grey', bd=0, command=mute).place(x=250, y=290)
        # Volume Bar
        self.scale = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, bg="red", bd=0 ,length=120, command=volume)
        self.scale.set(25)
        self.scale.place(x=300, y=290)


 

root = Tk()
obj = musicPlayer(root)
root.mainloop()