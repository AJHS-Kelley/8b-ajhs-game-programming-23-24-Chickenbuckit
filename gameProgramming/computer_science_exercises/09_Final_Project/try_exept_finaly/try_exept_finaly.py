#this is a method for testing corde and preventing crashes
#try -- exept -- else -- fynaly
try: #the code in this block is always exicuded
    my_variable = 1
    print(my_variabl)
except NameError: #this code will run if "try" fails
    print("\nsorry forgot that the coder is incompatent and can't spell\n")
except:
    print("I got know clue what broke here")
else: #this code will run if there is no errors
    print("code runs great\n good job champ")