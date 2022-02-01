from turtle import *

hideturtle()
bgcolor('black')
speed(12)
col = ('yellow', 'salmon', 'pink', 'orange', 'cyan','light green', 'blue')


for i in range(150):
    pencolor(col[i%6])
    circle(190-i/2, 90)
    left(90)
    circle(190-i/3, 90)
    left(60)
