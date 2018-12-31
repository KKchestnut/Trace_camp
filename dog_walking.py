# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def walk(self):
        return "%s is walking!" % (self.name)

    # Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    # Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:
    def __init__(self, pets):
            self.pets = pets

    def walk(self):
            for dog in self.dogs:
                print(dog.walk())


my_dogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

my_pets = Pets(my_dogs)

for dog in my_pets.pets:
    print("{}" .format(dog.walk()))
