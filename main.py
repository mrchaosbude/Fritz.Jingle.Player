#!/usr/bin/env python
import tkinter as tk
import scrape_jingle
import player
import os
from tkinter import messagebox
import shutil

jingletext, jinglelink = scrape_jingle.scrapy()

button_row = "3"
autop_vol_row = "2"

def start_play():
    """
    function to read the listbox selection
    and put the result in a label widget
    """
    # get selected line index
    index = listbox.curselection()[0]
    print(index)
    player.play(jinglelink[index])
    #t = Thread(target=player.play(jinglelink[index]), args=(True,))
    #t.start()
    # get the line's text
    seltext = listbox.get(index)
    # put the selected text in the label
    label['text'] = seltext

def start_play_e(event):
    start_play()

def voll_change(vol):
    vol = int(vol)/100
    player.vollumen(vol)


def on_exit():
    """When you click to exit, this function is called"""
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.destroy()
        player.stop()
        try:
            shutil.rmtree('./tmp')
        except:
            print("can't delite tmp")
        raise SystemExit


root = tk.Tk()
root.title("Fritz Jingle Player")
root.protocol("WM_DELETE_WINDOW", on_exit)
# use width x height + x_offset + y_offset (no spaces!)
#root.geometry("180x300+550+350")
# create a label (width in characters)
s = "Click on a cheese"
label = tk.Label(root, text=s,)
label.grid(row=0, column=1)
# create a listbox (height in characters/lines)
# give it a nice yellow background (bg) color
listbox = tk.Listbox(root, height=15, width=75, bg='yellow')
listbox.grid(row=1, column=0, columnspan=3)
# the Tkinter listbox does not automatically scroll, you need
# to create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=3, sticky='n' + 's')
listbox.configure(yscrollcommand=yscroll.set)

ap_check = 0
auto_play = tk.Checkbutton(root, text="Auto Play", variable=ap_check)
auto_play.grid(row=autop_vol_row, column=0)

vol_slider = tk.Scale(root, orient="horizontal", length=250, width=20, tickinterval=10,command=voll_change,)
vol_slider.grid(row=autop_vol_row, column=1, columnspan=2)
vol_slider.set(75)


play = tk.Button(root, text='Play', width=20, command=start_play)
play.grid(row=button_row, column=0)

stop = tk.Button(root, text='Stop', width=20, command=player.stop)
stop.grid(row=button_row, column=1)

quit = tk.Button(root, text='Quit', width=20, command=on_exit)
quit.grid(row=button_row, column=2)


for item in jingletext:
    listbox.insert('end', item)

# use left mouse click on a list item to display selection
listbox.bind('<Double-Button-1>', start_play_e)
root.mainloop()