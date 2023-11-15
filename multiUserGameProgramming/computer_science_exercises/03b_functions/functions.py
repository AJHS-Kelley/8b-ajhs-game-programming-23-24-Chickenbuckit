#casey boyce functions v0.3
import random
def example_function_a():# NO PARAMETERS
    count = 0
    num = int(input("How many times do you want me to wish you a happy birthday\n"))
    while count < num:
        print("Happy Birthday\n")
        count += 1

def example_function_b(num, count):# PARAMETERS
    count = 0
    num = int(input("How many times do you want me to wish you a happy birthday\n"))
    while count < num:
        print("Happy Birthday\n")
        count += 1

# IF A FUNCTION REQUARSE PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!!1!!11
# RUNNING A FUNCTION IS KNOWN AS CALLING IT

#example_function_a()
#example_function_b(5, 0)

def roll_dice(num_dice, size_dice):
    num_rolled = 0
    sum = 0
    while num_rolled < num_dice:
        roll = random.randint(1, size_dice)
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}")
        num_rolled += 1
    return sum # return will IMMEDIATELY exit a loop, function, if/elif/else block.

#roll_dice(4, 6)
#roll_dice(2, 12)

#player_str = roll_dice(3,6)
#player_dex = roll_dice(3,6)
#player_con = roll_dice(3,6)
#player_wis = roll_dice(3,6)
#player_int = roll_dice(3,6)
#player_cha = roll_dice(3,6)
#print(player_str)
#print(player_dex)
#print(player_con)
#print(player_wis)
#print(player_int)
#print(player_cha)

# or

def gen_stat():
    player_stat = [
        0, # str
        0, # dex
        0, # con
        0, # wis
        0, # int
        0] # cha
    i = 0
    while i < len(player_stat):
        player_stat[i] = roll_dice(3, 6)
        i =+ 1 
    print(player_stat)

gen_stat()