from turtle import *
bgcolor('black')
pencolor('yellow')
pensize(3)
fillcolor('red')
for i in range (5,0,-1):
    begin_fill()
    circle(i*10)
    rt(25)
    end_fill()
mainloop()    