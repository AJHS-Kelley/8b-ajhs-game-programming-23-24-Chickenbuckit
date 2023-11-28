#example game functions .py, Casey Boyce< v0.4
import random
import time
t = 0
#for
# = == += -=
titan_meter = True
self_destruct = ("Death imminent", "Are You Sure", "Self Destructing")

def countdown(t = 6):
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def drop_titan():
    print("Prepare for Titanfall")
    countdown(int(t))
    print("Good Work Pilot Now Hop In")

def titanfall(player_input, release_titan_key):
    while titanfall == True:
        if player_input == release_titan_key:
            drop_titan
        else:
            pass

def Blowing_up(self_destruct):
    for self_destruct in range(2):
        print(self_destruct)

while titan_meter == True:
    titanfall

