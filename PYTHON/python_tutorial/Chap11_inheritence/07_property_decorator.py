#property decorator


class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    
    @property                # this method is also known as getter method(@.getter)
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter      # this method is known as setter method(@.setter)
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)     # earlier totalsalary

e.totalSalary = 9000     # this the new totalsalary set by the user
print(e.salary)          # it will keep the salary similar to as it was ---> coz, formula in setter
print(e.salarybonus)     # it will change the remaining amount of the totalsalary as the salarybonus

