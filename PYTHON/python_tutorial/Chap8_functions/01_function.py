# Function is a group of ststements performing a specific task
'''
marks1 =[45, 36, 75, 68, 97]
percent1 = ((marks[0] + marks[1] + marks[2] + marks[3] +marks[4])/500)*100

marks2 =[75, 36, 57, 61, 79]
percent2 = ((marks[0] + marks[1] + marks[2] + marks[3] +marks[4])/500)*100

print(percent1, percent2)
'''
# ^^^ by above method, we can also solve the sum, but it is lengthy

# thus we solve above sum by function

def percent(marks):
    p =((marks[0] + marks[1] + marks[2] + marks[3] +marks[4])/500)*100
    return p

marks1 =[45, 36, 75, 68, 97]
percent1 = percent(marks1)

marks2 =[75, 36, 57, 61, 79]
percent2 = percent(marks2)

print( percent1, percent2)
