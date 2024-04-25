#this is a method for testing corde and preventing crashes
#try -- exept -- else -- fynaly
try: #the code in this block is always exicuded
    my_variable = 1
    print(my_variable)
    my_string = "Five"
    print(float(int(my_string)))
except NameError: #this code will run if "try" fails
    print("\nsorry forgot that the coder is incompatent and can't spell\n")
except:
    print("\nI got know clue what broke here\n")
else: #this code will run if there is no errors
    print("\ncode runs great\n good job champ\n")
finally:
    print("\ncode finnished runing\n")