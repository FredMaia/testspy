import turtle

# asdf = turtle.Screen()
# asdf.bgcolor("light green")
# asdf.title("Turtle")
asd = turtle.Turtle()

asd.color("blue") #the first value is the line color. The second one is the fill color

def createSquare():
    asd.forward(100)

    for i in range(3):
        asd.left (90)
        asd.forward (100)

createSquare()
createSquare()
turtle.done()

#Change the location without drawing a line
# asd.penup()
# asd.forward(150)
# asd.pendown()

# asd.begin_fill()

# asd.forward(100)
# asd.left(90)
# asd.forward(100)
# asd.left(90)
# asd.forward(100)
# asd.left(90)
# asd.forward(100)

# asd.end_fill()
