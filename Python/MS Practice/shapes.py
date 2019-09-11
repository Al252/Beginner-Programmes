import turtle

t_speed = turtle.speed()
t_position = turtle.pos()
t_direction = turtle.heading()
for shape in range(8):
    turtle.forward(50)
    turtle.dot(5, 'red')
    turtle.right(45)
print(turtle.pen().items())
turtle.pen(shown = False, pencolor = 'red')
