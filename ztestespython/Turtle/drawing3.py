import turtle

# draw = turtle.Turtle()
# draw.color("black")
# draw.speed(10)
# draw.getscreen().bgcolor("#994444")

# def star(draw):
#     for i in range(5):
#         draw.forward(200)
#         draw.left(216)

# star(draw)

# turtle.done()

colors = [ "pink","yellow","blue","green","white","red"]
sketch = turtle.Pen()
turtle.bgcolor("black")
for i in range(200):
   sketch.pencolor(colors[i % 6])
   sketch.width(i/100 + 1)
   sketch.forward(i)
   sketch.left(59)