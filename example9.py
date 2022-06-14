from turtle import *
s = Screen()
s.setup(500,500)
fillcolor('yellow')
pencolor('red')
speed('slowest')
for i in range(3):
    lt(120)
    penup()
    fd(80)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    penup()
    bk(80)
    pendown()

mainloop()
    
