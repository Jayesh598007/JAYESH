# write the class Vector
# overload '+' and '*' in it 


class vector:
    def __init__(self, vec):     # specifying the vector class
            self .vec = vec

    def __str__(self):       # printing the list in form of string
        str1 =""
        index =0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]     # '[]' is for not printing the last + in the row

    def __add__(self, vec2):    # for addition of 2 vectors
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return vector(newList)

    def __mul__(self, vec2):     #for multiplication of 2 vecors
        product = 0
        for i in range (len(self.vec)):
            product += self.vec[i] * vec2.vec[i]
        return product


v1 = vector([1, 3])   
v2 = vector([2, 6])
print(v1)    # print v1 vector
print(v2)     # print v2 vector

print()
print(v1 + v2)    # print additon of 2 vectors
print(v1 + v2)



 