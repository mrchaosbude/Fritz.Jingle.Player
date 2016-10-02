import os

import pygame.mixer as mix
import requests
import io
import pygame

#http://www.pygame.org/docs/ref/music.html#pygame.mixer.music.rewind
mix.init()
clock = pygame.time.Clock()

def __play_stream(url):
    print(url)
    r = requests.get(url, stream=True) #get the file
    mix.music.load(r.raw)
    mix.music.play()

    #clock = pygame.time.Clock() #macke a clock

    #while pygame.mixer.music.get_busy(): #check if music is playing
        #clock.tick(10)

    #pygame.quit()

def __play_download(url):
    global local_filename
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()# commented by recommendation from J.F.Sebastian

    mix.music.load(local_filename)
    mix.music.play()
    #return local_filename

def play(url):
    try:
        __play_stream(url)
    except:
        __play_download(url)


def stop():
    mix.music.stop()

test_url = 'http://media.rbb-online.de/frz/jingles/Fritz_Autokauf.MP3'
test_url = "http://media.rbb-online.de/frz/jingles/Fritz_90JahreRadio_01_(Gratulation).MP3"

if __name__ == "__main__":
    play(test_url)
    clock = pygame.time.Clock() #macke a clock

    while mix.music.get_busy(): #check if music is playing
        clock.tick(1)