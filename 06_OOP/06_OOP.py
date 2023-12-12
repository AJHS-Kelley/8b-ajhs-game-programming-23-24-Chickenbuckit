# object orented programming, Casey Boyce, v0.3

class Person: # use PASCALCASE for class_names 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.wekness = None
        self.nemesis = None

    #
    def __str__(self):
        return f"Name: {self.name}.\nThis person is {self.age} years old.\nThey weigh {self.weight}"
    
    def class_function(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class")
person1 = Person('Chavna "The Brutalizer"', 34, 175)
person2 = Person('Ur-Masi "The Massive"', 27, 547)
#print(person1)
#print(person2)

#if person1.weight > person2.weight:
#    print(f"{person1.name} weighs more than {person2.name}")
#elif person1.weight == person2.weight:
#    print("Each person weight the same.\n")
#else:
#    print(f"{person2.name} wieght more than {person1.name}")

person1.class_function()

# Changing Properties after Creation
print(person1.weight)
person1.weight = 215
print(person1.weight)

# Deleting properties -- DANGER
# THIS IS DOSE NOT 'RESET' A PROPERTY, IT DELETES IT
print(person1.name)
del person1.name
#print(person1.name)# CRASH :(

# DELETING OBJECTS -- DELETE THE OBJECT COMPLETLY
del person1

# ADDING PROPERTYS -- USE CAREFULLY
person2.weknesses = "Morgi Flies"
print(person2)
print(person2.weknesses)