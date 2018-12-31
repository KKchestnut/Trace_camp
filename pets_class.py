# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

        is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

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

my_dogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

my_pets = Pets(my_dogs)

#print ("I have  {} dogs" .format(len(my_pets.dogs)))
print("I have", len(my_pets.pets), "dogs.")

for dog in my_pets.pets:
    print("{} is {}" .format(dog.name, dog.age))

    dog.eat()

print("And they are all {}s, of course." .format(dog.species))

print("My dogs are not hungry" .format(dog.is_hungry))
