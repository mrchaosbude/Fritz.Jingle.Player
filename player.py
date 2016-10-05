import os
import wget
import pygame
import pygame.mixer as mix
import requests

#http://www.pygame.org/docs/ref/music.html #pygame.mixer.music.rewind

def __dummy_create(path):
    with open(path, 'a'):
        os.utime(path, None)

def isfile(filepath):
    """Test whether a path is a regular file"""
    try:
        f = open(filepath)
    except IOError:  # Note OSError is for later versions of python
        return False

    return True

def __play_stream(url):
    print(url)
    r = requests.get(url, stream=True) #get the file
    mix.music.load(r.raw)
    mix.music.play()

def __play_download(url): #tut nicht wie es soll
    global local_filename
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    r.close()

    mix.music.load(local_filename)
    mix.music.play()
    #return local_filename # tuht #

def __play_download2(url):
    global local_filename
    local_filename = url.split('/')[-1]

    try: ## erstellt tmp wenn nicht vorhanden
        os.makedirs("./tmp")
    except OSError:
        pass

    retval = os.getcwd() + "/tmp" #aktueller pfad + tmp
    os.chdir(retval) #wechsel in tmp

    if isfile(retval + "/" + local_filename) == False:
        print("file is not"+ retval + "/" + local_filename)
        wget.download(url)

    mix.music.load(local_filename)
    mix.music.play()
    os.chdir(os.pardir)


def play(url):
    mix.init()
    try:
        __play_stream(url)
        print("Play Stram")
    except:
        print("Play Download")
        __play_download2(url)

def set_vol(vol=1.0):
    mix.music.set_volume(vol)

def get_vol():
    return mix.music.get_volume()


def stop():
    mix.music.stop()
    mix.quit()
    pygame.quit()

test_url = 'http://media.rbb-online.de/frz/jingles/Fritz_Autokauf.MP3'
test_url2 = "http://media.rbb-online.de/frz/jingles/Fritz_90JahreRadio_01_(Gratulation).MP3"

if __name__ == "__main__":
    play(test_url)
    clock = pygame.time.Clock() #macke a clock

    while mix.music.get_busy(): #check if music is playing
        clock.tick(1)