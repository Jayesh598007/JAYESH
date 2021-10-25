# operator overloading
# operators in python can be overloaded with the dunder methods-->  '__add__' is called as dunder(double underscore)

'''
these are called when a given operator is used on the object:
to add-->     __add__
to substract-->   __sub__
to multiply-->    __mul__
to divide-->    __truediv__
'''


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets Add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets Multiply")
        return self.num * num2.num


# num = Number(4) 
# num2 = Number(5)
# sum = num + num2
# mul = num * num2
# print(sum)
# print(mul)




