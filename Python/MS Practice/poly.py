import turtle

def shape(sides, length):
    for line in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)
        for inner in range(sides):
            turtle.forward(length/2)
            turtle.right(360/sides)

polygon = shape(int(input('Number of sides: ')), int(input('Length of each side(In Pixels): ')))


turtle.done()
