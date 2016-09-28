#!/usr/bin/env python
import tkinter as tk
import scrape_jingle
import player
from threading import Thread
jingletext, jinglelink = scrape_jingle.scrapy()

def test_play():
    player.play("http://media.rbb-online.de/frz/jingles/Fritz_90JahreRadio_01_(Gratulation).MP3")

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


root = tk.Tk()
root.title("Cheeses")
# use width x height + x_offset + y_offset (no spaces!)
#root.geometry("180x300+550+350")
# create a label (width in characters)
s = "Click on a cheese"
label = tk.Label(root, text=s,)
label.grid(row=0, column=0)
# create a listbox (height in characters/lines)
# give it a nice yellow background (bg) color
listbox = tk.Listbox(root, height=15, width=75, bg='yellow')
listbox.grid(row=1, column=0, columnspan=3)
# the Tkinter listbox does not automatically scroll, you need
# to create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=3, sticky='n' + 's')
listbox.configure(yscrollcommand=yscroll.set)

play = tk.Button(root, text='Play', width=20, command=start_play)
play.grid(row=2, column=0)

stop = tk.Button(root, text='Stop', width=20, command=player.stop)
stop.grid(row=2, column=1)

quit = tk.Button(root, text='Quit', width=20, command=root.destroy)
quit.grid(row=2, column=2)

play = tk.Button(root, text='Play', width=20, command=test_play())
play.grid(row=3, column=0)


for item in jingletext:
    listbox.insert('end', item)

# use left mouse click on a list item to display selection
listbox.bind('<Double-Button-1>', start_play_e)
root.mainloop()