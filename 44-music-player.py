# Build a mp3 player step by step
# @2021/05/21

# tkinter reference
# https://docs.python.org/3/library/tkinter.html

# === 1st step: init a blank window ===
# https://pythonexamples.org/python-tkinter-set-window-size/
# import tkinter as tk

# gui = tk.Tk(className='Python Examples - Window Size')
# # set window size
# gui.geometry("400x200")
# gui.mainloop() 

# === 2th step: resize window with title ===
# https://pythonexamples.org/python-tkinter-window-background-color/

# import tkinter as tk

# gui = tk.Tk(className='Python Examples - Window Color')
# # set window size
# gui.geometry("400x200")
# #set window color
# gui.configure(bg='#2C2825')
# gui.mainloop() 

# === 3rd step: add one text/label ===
# https://www.geeksforgeeks.org/python-tkinter-text-widget/

# import tkinter as tk

# gui = tk.Tk(className='Python Examples - Label')

# bg_color = '#2C2825'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label
# l = tk.Label(gui, text = "This is a white label", bg = bg_color, fg = 'white')
# l.config(font =("Courier", 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# gui.mainloop() 

# === 4th step: add button ===
# install tkmacosx for fancy buttons on Mac pc
# Tkmacosx is a Python library extension to the Tkinter module that 
# let you change background color of the button on macOS.
# % pip3 install tkmacosx

# import tkinter as tk

# gui = tk.Tk(className='Python Examples - Button')

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn = tk.Button(gui, text = 'Pickup Music', highlightbackground = fg_color)
# btn.pack()

# gui.mainloop()

# === 5th step: add button click handler ===
# import tkinter as tk
# from tkinter import messagebox as mb


# def write_slogan():
#   print('--------------')
#   print("Tkinter is easy to use!")
#   mb.showinfo(message='You clicked the button!')

# gui = tk.Tk(className='Python Examples - Button Click')

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn = tk.Button(gui, text = 'Pickup Music', highlightbackground = fg_color, command = write_slogan)
# btn.pack()

# gui.mainloop()


# === 6th step: open files dialog ===
# import tkinter as tk
# from tkinter import filedialog as fd 

# mp3s = None

# def pick_mp3_files():
#   print('--------------')
#   global mp3s
#   mp3s = []
#   files = fd.askopenfiles(filetypes=[("Audio files", ".mp3")])
#   for file in files:
#     mp3s.append(file.name)
#   print(mp3s)

# gui = tk.Tk(className='Python Examples - Open Files')

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn = tk.Button(gui, text = 'Pickup Music', highlightbackground = fg_color, command = pick_mp3_files)
# btn.pack()

# gui.mainloop()


# === 7th step: display mp3 files in list ===

# import tkinter as tk
# from tkinter import filedialog as fd

# def onselect(evt):
#     # Note here that Tkinter passes an event object to onselect()
#     w = evt.widget
#     index = int(w.curselection()[0])
#     value = w.get(index)
#     print(value)

# gui = tk.Tk(className='Python Examples - Open Files')

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# # create a list box
# lb = tk.Listbox(gui, bg = '#56452d', fg = 'red', selectbackground = fg_color, height = 5)
# lb.insert(1, "Python")
# lb.insert(2, "Perl")
# lb.insert(3, "C")
# lb.insert(4, "PHP")
# lb.insert(5, "JSP")
# lb.insert(6, "Ruby")
# lb.pack(fill = tk.X, padx = 0, pady = 10)
# lb.bind('<<ListboxSelect>>', onselect)
# lb.selection_set( first = 0 ) #  select the first item

# gui.mainloop()


# === 8th step: display mp3 files in list  ===

# import tkinter as tk
# from tkinter import filedialog as fd

# ACTIVE_ITEM = None

# def onselect(evt):
#   global ACTIVE_ITEM
#   # Note here that Tkinter passes an event object to onselect()
#   w = evt.widget
#   index = int(w.curselection()[0])
#   if ACTIVE_ITEM == index:
#     return
#   ACTIVE_ITEM = index
#   value = w.get(index)
#   print(value)


# def pick_mp3_files():
#   global gui
#   mp3s = []
#   files = fd.askopenfiles(filetypes=[("Audio files", ".mp3")])
#   for file in files:
#     mp3s.append(file.name)
#   # create a list box
#   song_list = tk.Listbox(gui, bg = '#56452d', fg = 'red', selectbackground = fg_color, height = 5)
#   for i in range(len(mp3s)):
#     song_list.insert(tk.END, mp3s[i])
#   song_list.pack(fill = tk.X, padx = 0, pady = 10)
#   song_list.bind('<<ListboxSelect>>', onselect)

# gui = tk.Tk(className='Python Examples - Display mp3 files')

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn = tk.Button(gui, text = 'Pickup Music', highlightbackground = fg_color, command = pick_mp3_files)
# btn.pack()

# gui.mainloop()


# === 9th step: play mp3 music ===
# TODO: INSTALL dependencies:
# for windows:
# python -m pip3 install pyaudio pydub
# for Macosx:
# brew install portaudio && pip3 install pyaudio pydub

# import tkinter as tk
# from library.mp3player import PlayerOnce

# player = None

# def play_mp3_music():
#   global player, btn_play
#   # mp3_file_path = '/Users/liwenzhi/Music/anyone.mp3'
#   mp3_file_path = '/Users/liwenzhi/Music/video_bg_sounds/Piano_Elegant_Logo_layout.mp3'
#   player = PlayerOnce(mp3_file_path)
#   player.onEnd(lambda : btn_play.config(text = 'Play Music'))
#   player.play()
#   btn_play.config(text = 'Playing .... ')
  
  
# def stop_mp3_music():
#   global player, btn_play
#   if player == None:
#     return
#   player.stop()
#   btn_play.config(text = 'Play Music')


# def onClose():
#   global gui, player
#   print('Exited!')
#   if player != None:
#     player.stop()
#   gui.destroy()


# gui = tk.Tk()
# gui.title('Python Examples - Play mp3 file')
# gui.protocol('WM_DELETE_WINDOW', onClose)

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn_play = tk.Button(gui, text = 'Play Music', highlightbackground = fg_color, command = play_mp3_music)
# btn_play.place(x = 100, y = 60)

# btn_stop = tk.Button(gui, text = 'Stop Music', highlightbackground = fg_color, command = stop_mp3_music)
# btn_stop.place(x = 210, y= 60)

# gui.mainloop()


# === 10th step: play mp3 in list ===

# import tkinter as tk
# from tkinter import filedialog as fd
# from library.mp3player import PlayerOnce

# player = None

# ACTIVE_ITEM = None

# def play_mp3_music(mp3_file_path):
#   global player
#   player = PlayerOnce(mp3_file_path)
#   player.play()
  
  
# def stop_mp3_music():
#   global player
#   if player == None:
#     return
#   player.stop()


# def onClose():
#   global gui, player
#   print('Exited!')
#   if player != None:
#     player.stop()
#   gui.destroy()


# def onselect(evt):
#   global ACTIVE_ITEM
#   # Note here that Tkinter passes an event object to onselect()
#   w = evt.widget
#   index = int(w.curselection()[0])
#   if ACTIVE_ITEM == index:
#     return
#   ACTIVE_ITEM = index
#   mp3 = w.get(index)
#   stop_mp3_music()
#   play_mp3_music(mp3)


# def pick_mp3_files():
#   global gui, song_list
#   mp3s = []
#   files = fd.askopenfiles(filetypes=[("Audio files", ".mp3")])
#   for file in files:
#     mp3s.append(file.name)
#   # clear all before insert
#   song_list.delete(0, tk.END)
#   # insert new
#   for i in range(len(mp3s)):
#     song_list.insert(tk.END, mp3s[i])
#   if player is not None:
#     player.stop()

# gui = tk.Tk()
# gui.title('Python Examples - Play mp3 file')
# gui.protocol('WM_DELETE_WINDOW', onClose)

# bg_color = '#2C2825'
# fg_color = '#FCCA5D'
# # set window size
# gui.geometry('400x200')
# #set window color
# gui.configure(bg = bg_color)

# # Create label as title
# l = tk.Label(gui, text = 'Mini Mp3 Player', bg = bg_color, fg = fg_color)
# l.config(font =('Courier', 16))
# l.pack(fill = tk.X, padx = 0, pady = 10)

# btn = tk.Button(gui, text = 'Pickup Music', highlightbackground = fg_color, command = pick_mp3_files)
# btn.pack()

# # create a list box
# song_list = tk.Listbox(gui, bg = '#56452d', fg = 'red', selectbackground = fg_color, height = 6)
# song_list.pack(fill = tk.X, padx = 0, pady = 10)
# song_list.bind('<<ListboxSelect>>', onselect)

# gui.mainloop()


# === 11th step: refactor app to class structure

import tkinter as tk
from tkinter import filedialog as fd
from library.mp3player import PlayerOnce
from library.AnimatedGif import AnimatedGif

class Application():
  def __init__(self, master=None):
    self.master = master
    self.create_widgets()
    self.player = None
    self.ACTIVE_ITEM = -1

  def create_widgets(self):
    fg_color = '#FCCA5D'
    bg_color = '#000'
    # Create label as title
    self.app_title = tk.Label(self.master, bg = bg_color, fg = fg_color)
    self.app_title['text'] = 'Mini Mp3 Player'
    self.app_title.config(font =('Courier', 16))
    self.app_title.pack(fill = tk.X, padx = 0, pady = 4)
    # create anim
    self.visualizer = AnimatedGif(self.master, 'image/visualizer.gif')
    self.visualizer.config(bg = bg_color,)
    self.visualizer.pack(pady= 0,)
    # open files dialog
    self.choose_btn = tk.Button(self.master, highlightbackground = fg_color)
    self.choose_btn['text'] = 'Pickup Music'
    self.choose_btn['command'] = self.pick_mp3_files
    self.choose_btn.pack(pady= 10,)
    # create a list box
    self.song_list = tk.Listbox(self.master, bg = '#2C2825', fg = 'red', selectbackground = fg_color, height = 6)
    self.song_list.pack(fill = tk.X, padx = 0, pady = 0)
    self.song_list.bind('<<ListboxSelect>>', self.onselect)

  def pick_mp3_files(self):
    mp3s = []
    files = fd.askopenfiles(filetypes=[("Audio files", ".mp3")])
    for file in files:
      mp3s.append(file.name)
    # clear all before insert
    self.song_list.delete(0, tk.END)
    # insert new
    for i in range(len(mp3s)):
      self.song_list.insert(tk.END, mp3s[i])
    if self.player is not None:
      self.player.stop()

  # Note here that Tkinter passes an event object to onselect()
  def onselect(self, evt):
    w = evt.widget
    if len(w.curselection()) == 0:
      return
    index = int(w.curselection()[0])
    if self.ACTIVE_ITEM == index:
      return
    self.ACTIVE_ITEM = index
    mp3 = w.get(index)
    print('playing: {0}'.format(mp3))
    self.play_mp3_music(mp3)

  # ...
  def play_mp3_music(self, mp3_file_path):
    self.stop_mp3_music()
    self.player = PlayerOnce(mp3_file_path)
    self.player.play()
    self.visualizer.start()
    self.visualizer.config(pady= 18,)
    self.choose_btn.pack_forget()
  
  # ...
  def stop_mp3_music(self):
    if self.player == None:
      return
    self.player.stop()

  # ...
  def onClose(self):
    """
    close callback
    """
    print('Exited!')
    if self.player != None:
      self.player.stop()
    self.master.destroy()
# end of Application class


root = tk.Tk()
root.title('Mini Mp3 Player')
# set window size
root.geometry('400x200')
#set window color
root.configure(bg = '#000')
app = Application(root)
root.protocol('WM_DELETE_WINDOW', app.onClose)
root.mainloop()