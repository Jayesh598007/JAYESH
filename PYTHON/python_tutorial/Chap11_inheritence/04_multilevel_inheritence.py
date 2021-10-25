# Multilevel Inheritence
# when a child class becomes a parent for another child class

#   parent ------> child1-----> child2


class person:      # parent class
    country = "India"
    # the object of country and city will apply on all childs created under this parent class
    city = "Pune"

    def takebreath(self):
        print("I am breathing...")


class Employee(person):     # child1 class
    company = "Honda"

    def getSalary(self):
        print(f"The salary is {self.salary}")
        # it has its own company and breath statement, it will print its own

    def takebreath(self):
        print("I am an employee, and I am breathing again")


class Programmer(Employee):      # child2 class
    company = "Fiverr"

    def getSalary(self):
        print(f"no salary to programmer")
        # it has its own company and breath statement,and it will print its own

    def takebreath(self):
        print("I am a programmer, and I am continuosly breathing")


p = person()
e = Employee()
pr = Programmer()
print('**********')       # for space

p.takebreath()
e.takebreath()
pr.takebreath()
print('**********')       # for space

# print(p.company)     # throws error, as it doesnt has a company
print(e.company)
print(pr.company)
print('**********')       # for space

print(p.country)
print(e.country)
print(pr.country)
