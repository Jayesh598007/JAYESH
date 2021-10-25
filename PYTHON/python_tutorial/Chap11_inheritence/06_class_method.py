# to directly change the class attributes,without adding instance attributes, we need class method
# ie; Class method is a method which is bound to the class and not the object of the class
#  @classmethod decorator is used to create a class method 

class Employee:      # class
    company = "Camel"
    salary = 100
    location= "Mumbai"

    @classmethod    # class method is used like this
    def changesalary(self, sal):
        self.salary = sal

    @classmethod
    def changeloc(self, loc):
        self.location = loc

e = Employee()
print(e.salary)          # salary before changing
e.changesalary(455)      # salary changed to 455
print(e.salary)          # salary after changing for e object
print(Employee.salary)   # changed salary in 'class Employee'

e.changeloc("Delhi")
print(Employee.location)    # changed location in 'class Employee'
print(e.location)           # ^^ same output

