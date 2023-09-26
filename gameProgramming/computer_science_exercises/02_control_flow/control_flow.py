#Control flow, Casey Boyce, v0.7
# DECLERATION

fav_color = "green"
lucky_nuber = 8
my_gpa = 2.74
my_age = 16
pineapple_on_pizza = True

# if statement - check if this happened
if fav_color == "green" or "Green" or "GREEN":
    print("I like green to")
    
if my_gpa >= 2 :
    print("you are doing well I think your grate")

#if else if this dose not happen do this insted
if my_gpa >= 3.0 :
    print("good job your hon-a-roll")
else:
    print("ya suck this year but mabey next year")
if lucky_nuber <= 9 :
    print("your lucky number is only one digit")
else:
    print("your lucky number is two digits")
#elif if and else if this dose not work try this than go to the else statement
if my_age > 65:
    print("Thank you for working withus for so long you can now happly retire")
elif my_age > 50:
    print("Good job, bonus 1000 dollar added to yearly sallery")
else:
    print("Sorry, your not that old get back to work")
#1 if, 1 else, any amount of elif

#Nested if - elif - else Satements
if my_age > 15 :
    print("eligible for a liscense")
    if my_gpa >= 3.5 :
        print("you are abble to win a new car")
    elif my_gpa > 2.0:
        print("you are eligibale for 50% off of a car")
    else:
        print("hope you get a liscense")
else :
    print("Don't you have homework that you have not finnished")

#when doing if elif else satements BIGGER NUMBERS first then small numbers
if my_gpa > 1.5 :
    print("you may fall down this year but allways get back up")
elif my_gpa > 2.0 :
    print("on track good job")
elif my_gpa > 3.0 :
    print("you may not just succsed you will thrive my friend")
elif my_gpa > 3.99 :
    print("holy crap, you are doin' tubular my dude")
else:
    print("3Rr0r")

#while loop, while this is happing then this happens
#itteration = one trip complete thrugh a loop
x = 0
while x <= 100:
    print(f"X is equeal to {x}")
    x += 1

# (parintases)
# [square Brakets]
# <angled Brakets>
# {Braces}

while x >= 0 :
    print(f"X is equeal to {x}")
    x -= 1
#for loop, this loop runs foor this meny tymes
for i in range(10): #i = iterable varitable
    print(i)

print("even or odd loop")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("even")
    else:
        print("odd")