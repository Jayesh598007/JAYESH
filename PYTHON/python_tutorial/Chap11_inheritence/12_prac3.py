# use property dcorator
#  salaryAfterIncrement  = salary *increment


class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment      # for printing the salary after increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary      # for printing the increment


e = Employee()          # e is an object
print(e.salaryAfterIncrement)         # salary with initial increment
print(e.increment)         # increment as it was before

e.salaryAfterIncrement = 2000             # after setting the new salary after increment
print(e.increment)       # increment after the new salary
