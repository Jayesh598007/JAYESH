

class vector:
    def __init__(self, vec):     # specifying the vector class
            self .vec = vec

    def __str__(self):       # printing the list in form of string
        str1 =""
        index =0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __len__(self):
        return len(self.vec)

v1 = vector([1, 3])   
v2 = vector([2, 6])
print(v1)
print(v1)
print(len(v1))    # print len of v1 vector
print(len(v2))     # print len of v2 vector

