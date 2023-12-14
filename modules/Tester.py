import dice
# Dont Import random if using things that have random in it
roll1 = dice.display(1, 6)
roll2 = dice.display(1, 6)

if dice.is_double(roll1, roll2):
    print("You Rolled A Double, Please, Go Again")
else:
    print("Sorry, This Is Not A Double")