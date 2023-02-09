import turtle
def polygon(sides,sidelength):
    angle = 360.0/sides
    print(angle)
    for i in range(sides):
        turtle.forward(sidelength)
        turtle.right(angle)
