from random import randint
from turtle import Turtle

angle = float(randint(60, 120))
move = 5
points = 0

ball = Turtle()
ball.shape("circle")
ball.speed(0)

platform = Turtle()
platform.shape("square")
platform.shapesize(1, 5, 1)
platform.up()
platform.speed(0)
platform.sety(-300)

target = platform.clone()
target.ht()

screen_width = ball.getscreen().window_width()
screen_height = ball.getscreen().window_height()
platform.getscreen().onclick(target.goto)

while True:
    ball.setheading(angle)
    ball.fd(move)
    if abs(ball.xcor()) > screen_width / 2:
        angle = 180 - angle
    elif ball.ycor() > screen_height / 2:
        angle = 360 - angle
    elif ball.ycor() < screen_height / -2:
        platform.write(f"Przegrałeś. Liczba punktów: {points}")
        platform.ht()
        platform.getscreen().exitonclick()
    elif (
        abs(ball.xcor() - platform.xcor()) < 80
        and abs(ball.ycor() - platform.ycor()) < 15
    ):
        points += 1
        angle = 360 - angle + randint(-30, 30)

    if platform.distance(target) > move:
        platform.getscreen().delay(1)
        platform.setheading(platform.towards(target))
        platform.tiltangle(-platform.towards(target))
        factor = 1 - 0.01*points
        platform.fd(move*factor)
    else:
        platform.getscreen().delay(2)
        
