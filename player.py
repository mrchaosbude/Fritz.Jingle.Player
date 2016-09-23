import pygame
import requests
from time import sleep

#http://www.pygame.org/docs/ref/music.html#pygame.mixer.music.rewind

def player(url):
    pygame.mixer.init()
    r = requests.get(url, stream=True)
    pygame.mixer.music.load(r.raw)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        sleep(1)

test_url = 'http://media.rbb-online.de/frz/jingles/2010/Fritz_Augentinitus.mp3'

if __name__ == "__main__":
    player(test_url)