# Dice Rolling mod, Casey Boyce, v0.3
import random

def display(num_dice, size_dice): # Works of 12-14-23
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum {sum}\n")
        num_rolled += 1
    return sum

def roll(num_dice, size_dice): # Works of 12-14-23
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        sum += roll
        num_rolled += 1
    return sum

def is_double(roll1, roll2):
    if roll1 == roll2:
        is_double = True
    else:
        is_double = False
    return is_double

def explode_dice(roll, size_dice):
    if roll == size_dice:
        explode_dice = True
    else:
        explode_dice = False
    return explode_dice