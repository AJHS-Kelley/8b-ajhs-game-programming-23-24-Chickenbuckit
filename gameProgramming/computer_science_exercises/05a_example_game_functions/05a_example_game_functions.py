#example game functions .py, Casey Boyce< v0.4
import random
import time
player_input = "v"
self_destruct = ("                                                        Death imminent", "                                                   Are You Sure", "                                             Self Destructing")
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
    print("                                                  Prepare for Titanfall")
    countdown()
    print("                                                  Good Work Pilot! Now Hop In")
    titan_meter = False  # Set titan_meter to False to exit the loop

def titanfall():
    global titan_meter
    player_input = input('                                                Press "V" to drop your titan: ')
    if player_input.upper() == "V":
        drop_titan()
    else:
        quit("                                               Input Error Exiting Code")
        
def Blowing_up(self_destruct):
    time.sleep(1)
    print("                Titan:                    Engaging multiple hostile Titans")
    time.sleep(random.randint(3, 6))
    print("                                           Pilot Your titan is taking too much damage!\n                                                 Get out or your going to die!")
    time.sleep(5)
    print('                                                  Press "X" to eject from Titan')
    for phase in self_destruct:
        time.sleep(2)
        print(phase)


while titan_meter:
    titanfall()
    if player_input.upper() == "V":
        titan_meter = False
    else:
        quit("                                               Input Error Exiting Code")
    Blowing_up(self_destruct)

# Code Review by Ryan Kelley 