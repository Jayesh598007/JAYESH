#  __init__() is a func which runs as soon as the object is created
# it is also known as constructor
 
class Employeee:
    company= "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def details(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The subunit of employee is {self.subunit}")

        
harry = Employeee("Harry", "10089", "Youtube")
# harry - Employeee()  --> this will throw an error
harry.details()



