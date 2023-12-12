# object orented programming, Casey Boyce, v0.2

class Person: # use PASCALCASE for class_names 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    #
    def __str__(self):
        return f"Name: {self.name}.\nThis person is {self.age} years old.\nThey weigh {self.weight}"
person1 = Person('Chavna "The Brutalizer"', 34, 175)
person2 = Person('Ur-Masi "The Massive"', 27, 547)
print(person1)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.name}")
elif person1.weight == person2.weight:
    print("Each person weight the same.\n")
else:
    print(f"{person2.name} wieght more than {person1.name}")