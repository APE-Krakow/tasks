import turtle
from math import sqrt, cos, tan, pi

def get_shape_info():
    shape = turtle.textinput("Nazwa", "Podaj nazwę kształtu")
    x = turtle.numinput("x", "Podaj współrzedną x")
    y = turtle.numinput("y", "Podaj współrzedną y")
    return (shape, x, y)

def draw_polygon(x, y, sides):
    if sides > 2:
        turtle.teleport(x, y)
        angle = 180 * (sides-2) / sides

        for i in range(0, sides):
            turtle.lt(180-angle)
            turtle.fd(calculate_side(sides))

def calculate_side(sides, height = 100):
    if sides%2 == 0:
        return height * tan(pi/sides)
    else:
        return 2 * height * tan(pi/sides) * cos(pi/sides) / (1+cos(pi/sides))
        

for i in range(10):
    draw_polygon(i*50, 0, i+3)


turtle.done()