#Multiplication of complex number
# complex no. is 2i + 3j + 4k
# Multiplication:---->    (a+bi)(c+di) = (ac-bd) + (ad+bc)i


class Complex:
    def __init__(self, r, i):    
        self.real = r
        self.imaginary = i

    def __add__(self, c):    # add method for complex nos.
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):    # add method for complex nos.
        mulReal = self.real*c.real-self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary+self.imaginary*c.real
        return Complex(mulReal, mulImg)
   
    def __str__(self):      # to return/print in string 
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(1, 4)   # complex nos
c2 = Complex(8, 5)

print(c1 + c2)    # addition

print(c1 * c2)     # multiplication

