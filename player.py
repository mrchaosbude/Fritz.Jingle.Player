import pygame
import requests

#http://www.pygame.org/docs/ref/music.html#pygame.mixer.music.rewind

def player(url):
    pygame.mixer.init()
    r = requests.get(url, stream=True) #get the file
    pygame.mixer.music.load(r.raw)
    pygame.mixer.music.play()
    clock = pygame.time.Clock() #macke a clock

    while pygame.mixer.music.get_busy(): #check if music is playing
        clock.tick(1)

    pygame.quit()

test_url = 'http://media.rbb-online.de/frz/jingles/Fritz_Autokauf.MP3'

if __name__ == "__main__":
    player(test_url)