#number guess, casey boyce, v0.4
#select numbrey
#nuber guessed by person
# tell point value
#Tell if wrong
    # tell if guess bad
    # tell if high/low
    # tell numbrey guess left
#what happen when guess right
    # tell if correct
    # give dem point
# Run out of guesses?
    #compuder gets point
    #give point to puder
#if puder has 3 points den puder wins
import random
import randint
#declerations
max_range = -1
min_range = -1
diffacolty = ""
secerate_nuber = -7
point_p = 0
point_c = 0
guess_nuber = -1
player = ""
print(""" .~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
          |                                           |
          | WELLCOME                                  |
          |                  TO                       |
          |      GUESS                    A           |
          |               NUMBER                      |
          |                                           |
          |                               Casey Boyce |
          |                               @)@# 2023   |
          `~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`
 """)

player =  input("What Do You Want Me To Call You?\nType Your Name in, then Press enter")
print("You Need To Guess A Number; You Have 5 Guesses. \nIf You Guess Right You Get A Cookie, \nIf You Can't Guess It In 5 Guesses Then The Computer Gets Your Cookies")
is_correct = input("Please type yes if correct, if no type no.\n")
if is_correct == "yes" or "YES" or "Yes" or "yES" or "YeS" or "YEs" or "yEs" or "yeS":
    print("Ok {player}, Lets Rock!")
else:
    player =  input("What Do You Want Me To Call You?\nType Your Name in, then Press enter")
while point_p != 3 and point_c != 3 :
    print(f"Player score: {point_p}\n Computer score: {point_c}")
    secerate_nuber = random.randint(min_range,max_range)
    guess_nuber = 0
    for guesses in range(5):
        print(f"You {5 - guess_nuber}")