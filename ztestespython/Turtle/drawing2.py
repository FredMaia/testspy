import turtle

asd = turtle.Turtle()
asd.color("red", "yellow")
asd.speed(10)

asd.begin_fill()
for i in range(50):
    asd.forward(300)
    asd.left(170)
asd.end_fill()

turtle.done()