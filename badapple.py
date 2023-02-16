from datetime import datetime
import time
import os
import pygame
import pydub
from pydub import AudioSegment
file= open(r"C:/Users/User/Desktop/ALL Python projects/BadAppleWithPython/data.txt","r")
lines = file.readlines()
current_l = 1
start_time = time.perf_counter()

def start_aud():
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('badapple.mp3')
    pygame.mixer.music.play(-2)
    
       


def start_vid():
    start_aud()
    current_l = 1
    start_aud()
    start_time = time.perf_counter()
    for frame in range(1, 6572):
        now = datetime.now()
        count = 100
        seconds = now.second
        frame_data = lines[current_l]
        print(frame_data[0:count-1])
        for c in range(0, 36):
              print(frame_data[count-99:count])
              count = count + 100
            
            

        
        
        timer = round(abs((start_time - time.perf_counter())), 1)
        current_l = seconds*30
        current_l = int(timer*30)
        print("timer: "+ str(timer))
        
        print(str(current_l)+ "/6572")
        time.sleep(1/25)
        

        os.system('CLS')

        



    

start_vid()


