#https://www.youtube.com/watch?v=0WldBjYRlaI
#added image export from Google AI suggestions


import turtle
from PIL import Image
import matplotlib.pyplot as plt

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(10)
#Initializations and definition
triquetra_size = 290
center = (0, -45)
line_width = triquetra_size * 0.0866
circle_radius = triquetra_size * 0.7
def arc(x):    
    t.fillcolor("black")
    t.begin_fill()
    t.circle(x, 180)        
    t.left(90)
    t.forward(line_width)
    t.left(90)
    t.circle(-x * 0.9, 180)
    t.end_fill()
#Execution
#Circle
for color in ["black", "white"]:
    t.penup()
    t.goto(center)
    t.forward(circle_radius)    
    t.left(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(circle_radius)
    t.end_fill()
    circle_radius = circle_radius - line_width
    t.right(90)        
t.right(30)
#arcs
for i in range(3):    
    t.penup()
    t.goto(center)    
    t.forward(triquetra_size)
    t.left(120)
    t.pendown()
    arc(triquetra_size * 0.866)
    t.right(60)
t.hideturtle()
#screen.exitonclick()

# Save the drawing as a PostScript file
canvas = screen.getcanvas()
canvas.postscript(file="turtle_drawing.eps")

# Convert the PostScript file to PNG using Pillow
#img = Image.open("turtle_drawing.eps")
#img.save("turtle_drawing.png", "png")

# Convert the canvas to a figure
fig = plt.figure()
fig.canvas.draw()
fig.canvas.blit(canvas.bbox)

# Save the figure as a PNG file
plt.savefig("turtle_drawing.png")