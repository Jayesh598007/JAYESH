from turtle import *

bgcolor('black')
speed(10)
hideturtle()

col= ['yellow', 'red', 'white', 'orange', 'blue']
c = 0

for i in range(50):
    forward(i*10)
    right(144)
    color(col[c])
    if c==4:
        c=0
    else:
        c+=1