class Animals():
    def breathe(self):
        print("breathing")
    def move(self):
        print("moving")
    def eat_food(self):
        pass

class Mammals(Animals):
    def fywm(self):
        print("feeding young") 

class Giraffes(Mammals):
    def elft(self):
        print("eating leaves")
    def dance(self):
        for i in range(3):
            print("left foot forward")
            print("right foot forward")
            print("left foot back")
            print("right foot back")
            


# import turtle
# avery = turtle.Pen()
# kate = turtle.Pen()
# jacob= turtle.Pen()
# avery.forward(50)
# avery.right(20)
# avery.forward(20)
# kate.left(40)
# kate.forward(87)
# jacob.left(123)
# jacob.forward(63)
# jacob.right(123)
# jacob.forward(25)
# jacob.right(102)


# 1
reginald=Giraffes()
reginald.dance()    

#2
import turtle
a= turtle.Pen()
e= turtle.Pen()
w= turtle.Pen()
t= turtle.Pen()
l= turtle.Pen()
a.backward(120)
e.left(90)
e.forward(50)
e.right(90)
e.forward(55)
w.right(90)
w.forward(50)
w.left(90)
w.forward(55)
t.forward(10)
t.right(90)
t.forward(25)
t.left(90)
t.forward(35)
l.forward(10)
l.left(90)
l.forward(25)
l.right(90)
l.forward(35)