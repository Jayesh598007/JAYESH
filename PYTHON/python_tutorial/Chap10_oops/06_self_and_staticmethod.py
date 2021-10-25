class Employeee:
    company= "Google"
    def getsalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod    #static method doent use self in the brackets 
    def greet():
        print("Good morning, sir")

    @staticmethod
    def time():
        print("The time is 9 am")

# for harry
harry = Employeee()
harry.greet()                # greeting
harry.salary = 100000
harry.getsalary("Thanks!")   # statement in bracket betn "  " is the signature


# for rajni
rajni= Employeee()
rajni.salary = 200789
rajni.getsalary("Thanks!")     # this quote is similar to 'Employee.getsalary(rajni)'
rajni.time()    # function calling for time

