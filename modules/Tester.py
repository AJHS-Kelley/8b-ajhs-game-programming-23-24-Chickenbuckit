import dice
import perfmon 
# Dont Import random if using things that have random in it
start = perfmon.exec_start
stop = perfmon.exec_stop


roll1 = dice.display(1, 6)
roll2 = dice.display(1, 6)

if dice.is_double(roll1, roll2):
    print("You Rolled A Double, Please, Go Again")
else:
    print("Sorry, This Is Not A Double")

if dice.explode_dice(roll1, 6):
    print("This Roll Exploded\n")
    roll1 += dice.roll(1, 6)
    print(roll1)