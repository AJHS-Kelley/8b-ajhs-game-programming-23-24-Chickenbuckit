#example game functions .py, Casey Boyce< v0.4
import random
import time
self_destruct = ("                                                  Death imminent", "                                                  Are You Sure", "                                                  Self Destructing")
titan_meter = True

def countdown(t = 6):
    t = random.randint(5, 7)
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def drop_titan():
    global titan_meter
    countdown()
    print("                                                  Good Work Pilot! Now Hop In")
    titan_meter = False  # Set titan_meter to False to exit the loop

def titanfall(player_input):
    global titan_meter
    player_input = input('                                                  Press "V" to drop your titan: ')
    if player_input.upper() == "v":
        drop_titan()
    else:
        return
        
def Blowing_up(self_destruct):
    print("                                                  Pilot Your titan is taking too much damage!\n                                                  Get out or your going to die!")
    time.sleep(5)
    print('                                                  Press "E" to eject from Titan')
    for phase in self_destruct:
        time.sleep(2)
        print(phase)


while titan_meter:
    titanfall()
    if player_input.upper() == "v":
        print("                                                  Prepare for Titanfall")
        titan_meter = False
    else:
        break
    Blowing_up(self_destruct)

# Code Review by Ryan Kelley 