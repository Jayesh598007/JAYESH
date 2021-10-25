#create a multi level inheritence

class Animals:
    animalType = "Mammal"

class pet:
    color = "white"

class dog:
    @staticmethod
    def bark():
        print("Bow Bow")

d = dog()
d.bark()

