# object orented programming, Casey Boyce, v0.1

class Person: # use PASCALCASE for class_names 
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    #
    def __str__(self):
        return f"Name: {self.name}.\nThis person is {self.age} years old.\nThey weigh {self.weight}"
person1 = Person('Chavna "The Brutalizer"', 34, 175)
print(person1)