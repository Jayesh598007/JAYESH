# class is created to make programming easy
# to ensure that the codes should be placed within same class
# it reduces the confusion and enhances  the accessibility


# it works on DRY principle (Donot Reapeat Yourself)

class Alphabet:
    pass

class Number:    
    def sum(self):
        return self.a + self.b


# thus here, it ensure that below codes are being saved in th 'class Number'  and not in 'class Alphabet'

num = Number()    # object 'num' is instantiated in class 'Number'
# memory is located in class after adding an object to it
num.a =12
num.b= 34
print("The sum of a nd b is:", num.sum())
