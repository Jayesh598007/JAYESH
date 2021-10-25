class person:      # parent class
    country = "India"
    def __init__(self): 
        print("Initialising Person...\n")

    def takebreath(self):
        print("I am breathing...")


class Employee(person):     # child1 class
    company = "Honda"
    def __init__(self): 
        super().__init__()      # this helps in printing the object of the super class(its parent class*1)
        print("Initialising Employee...\n")

    def getSalary(self):
        print(f"The salary is {self.salary}")
    def takebreath(self):
        super().takebreath()      # this helps in printing the object of the super class(its parent class*1)
        print("I am an employee, and I am breathing again")


class Programmer(Employee):      # child2 class
    company = "Fiverr"
    def __init__(self): 
        super().__init__()       # this helps in printing the object of the super class(its parent class*2)
        print("Initialising Programmer...\n")

    def getSalary(self):
        print(f"no salry to programmer")
    def takebreath(self):
        super().takebreath()     # this helps in printing the object of the super class(its parent class*2)
        print("I am a programmer, and I am continuosly breathing")

# p = person()
# p.takebreath()
# print("******")
# e = Employee()
# e.takebreath()
# print("********")
pr = Programmer()    # printing the super method of programmer (ie, statement of: parent class + child1 class + child class2))
# pr.takebreath() 

  


