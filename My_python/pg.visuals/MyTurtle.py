from turtle import *
shape('turtle')
def squares(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)
j = 0
while j <= 360:
    squares(40)
    right(5)
    j += 5
ts = getscreen()
ts.getcanvas().postscript(file="rtfm.eps")
done()