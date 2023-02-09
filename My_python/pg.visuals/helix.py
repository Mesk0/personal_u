from turtle import *
import polygon
i = 0
length = 0
while i <= 360:
    polygon.polygon(4, length)
    right(5)
    length += 5
    i += 5
