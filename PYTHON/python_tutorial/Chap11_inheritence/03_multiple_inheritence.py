# Multiple inheritence
# it occurs when the child class inherits more than one(multiple) base class
   
    # parent -------> child1
    #        `------> child2

class Employee:     # base class 1
    company= "Visa"
    eCode = 120

class Freelancer:    # base class 2
    company = "Google"
    level = 2

    def upgradelevel(self):    # function for upgrading the level
        self.level = self.level + 1

class Programmer(Employee, Freelancer):   # child class, which inherits both the base classes, sequencing @1employee and @2freelancer
    name= "rohit"

p = Programmer()
print(p.company)     # printing the company, (this will only print the company for the Employee as it is @ seq 1)
print(p.level)       # level at start  -->2
print()            # for space

p.upgradelevel()    # upgrading the level by 1
print(p.level)       # level after upgrading --->3
print(p.name)     # printing the name


