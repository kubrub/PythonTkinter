'''
This code draws the machine using the turtle's library
'''


from turtle import*


def draw_rect(coordinate_forward, coordinate_turns, coordinate_forward_height=None):
    if coordinate_forward_height is None:
        coordinate_forward_height = coordinate_forward
    forward(coordinate_forward)
    left(coordinate_turns)
    forward(coordinate_forward_height)
    left(coordinate_turns)
    forward(coordinate_forward)
    left(coordinate_turns)
    forward(coordinate_forward_height)
    
   
    
    
#initiliaze turtle
shape ('circle')
color('blue')
width(5)

#малюю квадрат, перша частина машинки
fillcolor('blue')
begin_fill()
draw_rect(75, 90)
'''for i in range(4):
    left(90)
    forward(75)
'''
end_fill()

#прямокутник, 2 частина машинки
color("green")
fillcolor('green')
begin_fill()
draw_rect(70, 90, 155)
end_fill()

#перейти до іншої координати -- можна використати goto
up()
backward (125)
left(90)
forward(20)
down()

#квадрат, швидше за все вікно
color("yellow")
fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(35)
    right(90)
end_fill()

#перейти до іншої координати -- можна використати goto
up()
forward(55)
left(90)
backward(20)
left(90)
down()

color("red")
fillcolor('red')
begin_fill()

for i in range(2):
    left(90)
    forward(105)
    left(90)
    forward(150)
   
end_fill()
goto(,)
'''up()
left(90)
forward(150)
left(90)
forward(90)
down()'''
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
