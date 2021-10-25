# adding a static method to greet a user, in prac2

class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number **0.5} ")

    def cube(self):
        print(f"The square of {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("*********Hello, welcome to the calculator********")

Value = int(input("Enter the value:"))
a = calculator(Value)
a.greet()
a.square()
a.squareroot()
a.cube()
