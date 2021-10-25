# write a '__str__' method to print vectors in form of "3i + 4j +7k"
class vector:
    def __init__(self, vec):     # specifying the vector class
            self .vec = vec

    def __str__(self):       # printing the list in form of string
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "


v1 = vector([1, 3, 4])   
v2 = vector([2, 6, 9])
print(v1)
print(v2)