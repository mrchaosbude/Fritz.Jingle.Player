import pygame.mixer as mix
import requests

#http://www.pygame.org/docs/ref/music.html#pygame.mixer.music.rewind
mix.init()

def play(url):
    r = requests.get(url, stream=True) #get the file
    mix.music.load(r.raw)
    mix.music.play()

    #clock = pygame.time.Clock() #macke a clock

    #while pygame.mixer.music.get_busy(): #check if music is playing
        #clock.tick(10)

    #pygame.quit()


def stop():
    mix.music.stop()

test_url = 'http://media.rbb-online.de/frz/jingles/Fritz_Autokauf.MP3'

if __name__ == "__main__":
    play(test_url)