'''
This code draws the machine using the turtle's library
'''
from turtle import*
shape ('circle')
color('blue')
width(5)
fillcolor('blue')
begin_fill()
for i in range(4):
    left(90)
    forward(75)

end_fill()

color("green")
fillcolor('green')
begin_fill()
forward(70)
left(90)
forward(155)
left(90)
forward(70)
left(90)
forward(155)
end_fill()

up()
backward (125)
left(90)
forward(20)

down()
color("yellow")
fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(35)
    right(90)
end_fill()
up()

forward(55)
left(90)
backward(20)
left(90)
down()

color("red")
fillcolor('red')
begin_fill()

left(90)
forward(105)
left(90)
forward(150)
left(90)
forward(105)
left(90)
forward(150)
end_fill()
up()
left(90)
forward(150)
left(90)
forward(90)
down()
color("black")
fillcolor("black")
begin_fill()

circle (20)
up()
backward(170)
down()
circle(20)
end_fill()

up()
left(90)
forward(95)
left(90)
forward(40)
down()
color("yellow")
fillcolor("yellow")
begin_fill()
circle(10)
end_fill()
up()
left(90)
forward(125)
down()
width(5)
color("black")
write("Car by Nastia Kovalchuk")