import matplotlib.pyplot as plt
import math
from matplotlib.patches import Arc


def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return [(x3, y3), (x4, y4)]

def find_center(x1, y1, x2, y2, x3, y3):
  """Finds the center (centroid) of a triangle.

  Args:
    x1, y1: Coordinates of the first vertex
    x2, y2: Coordinates of the second vertex
    x3, y3: Coordinates of the third vertex

  Returns:
    A tuple containing the x and y coordinates of the centroid.
  """

  center_x = (x1 + x2 + x3) / 3
  center_y = (y1 + y2 + y3) / 3

  return center_x, center_y

#Initializations and definition
#User defines radius and offsetY
radius = 10 #radius of the 3 arcs that make up the triquetra
print (f"radius = {radius}")
offsetYPercentOfRadius = 1.2 # a value > 0 and < 2
line_width = 10
includeCentralCircle = True
central_radius = 0.8 * radius
if includeCentralCircle:
    output_file = f"IntersectingCircles_YOffset_{offsetYPercentOfRadius}_withCenterCircle_{central_radius}.png"
else:
    output_file = f"IntersectingCircles_YOffset_{offsetYPercentOfRadius}_noCenterCircle.png"

#Calculated Paremeters
#Define Circles
offsetY = offsetYPercentOfRadius * radius 
offsetX = offsetY*math.tan(math.radians(30))
print (f"offsetX = {offsetX}")
print (f"offsetY = {offsetY}")
circleCenterBot = [0,0]
#circleCenterUpperRight = [radius - offsetX, offsetY] 
#circleCenterUpperLeft = [-radius + offsetX, offsetY]
circleCenterUpperRight = [offsetX, offsetY] 
circleCenterUpperLeft = [-offsetX, offsetY]
print (f"circleCenterBot = {circleCenterBot}")
print (f"circleCenterUpperRight = {circleCenterUpperRight}")
print (f"circleCenterUpperLeft = {circleCenterUpperLeft}")
#Define intersections of the circles
intersectionsBottomAndUR = get_intersections(circleCenterBot[0],circleCenterBot[1],radius,circleCenterUpperRight[0],circleCenterUpperRight[1],radius)
print (f"intersectionsBottomAndUR = {intersectionsBottomAndUR}")
rightArcRightIntersectionMax = max(intersectionsBottomAndUR, key=lambda coord: coord[0])
rightArcRightIntersectionMin = min(intersectionsBottomAndUR, key=lambda coord: coord[0])
intersectionsBottomAndUL = get_intersections(circleCenterBot[0],circleCenterBot[1],radius,circleCenterUpperLeft[0],circleCenterUpperLeft[1],radius)
print (f"intersectionsBottomAndUL = {intersectionsBottomAndUL}")
leftArcLeftIntersectionMin = min(intersectionsBottomAndUL, key=lambda coord: coord[0])
leftArcLeftIntersectionax = max(intersectionsBottomAndUL, key=lambda coord: coord[0])
intersectionsULAndUR = get_intersections(circleCenterUpperLeft[0],circleCenterUpperLeft[1],radius,circleCenterUpperRight[0],circleCenterUpperRight[1],radius)
print (f"intersectionsULAndUR = {intersectionsULAndUR}")
topArcTopIntersectionMax  = max(intersectionsULAndUR, key=lambda coord: coord[1])
topArcBottomIntersectionMin  = min(intersectionsULAndUR, key=lambda coord: coord[1])

central_center = (find_center(topArcTopIntersectionMax[0],topArcTopIntersectionMax[1],
                             leftArcLeftIntersectionMin[0],leftArcLeftIntersectionMin[1],
                             rightArcRightIntersectionMax[0],rightArcRightIntersectionMax[1]))
print (f"central_center = {central_center}")
#Define the 3 arcs from the interection points using start and end angles
    #Since the itersection points are relative to 0,0, I had to offset the values relative to the centers of the UL and UR circles when calculating the angles
arcs = [
    {"center": circleCenterBot, 
     "theta1": math.degrees(math.atan2(rightArcRightIntersectionMax[1],rightArcRightIntersectionMax[0])), 
     "theta2": math.degrees(math.atan2(leftArcLeftIntersectionMin[1],leftArcLeftIntersectionMin[0]))}, 
     #"theta2": math.degrees(math.atan(leftArcLeftIntersectionMin[0]/leftArcLeftIntersectionMin[1]))},  # Bottom circle
    {"center": circleCenterUpperRight, 
     "theta1": math.degrees(math.atan2(topArcTopIntersectionMax[1] - circleCenterUpperRight[1],topArcTopIntersectionMax[0] - circleCenterUpperRight[0])), 
     "theta2": math.degrees(math.atan2(rightArcRightIntersectionMax[1] - circleCenterUpperRight[1],rightArcRightIntersectionMax[0] - circleCenterUpperRight[0]))},  # Top right circle
    {"center": circleCenterUpperLeft,
     "theta1": math.degrees(math.atan2(leftArcLeftIntersectionMin[1] - circleCenterUpperLeft[1],leftArcLeftIntersectionMin[0] - circleCenterUpperLeft[0])), 
     "theta2": math.degrees(math.atan2(topArcTopIntersectionMax[1] - circleCenterUpperLeft[1],topArcTopIntersectionMax[0] - circleCenterUpperLeft[0]))},  # Top left circle
]


print (f"theta1ArcCenterBot {arcs[0]["theta1"]}")
print (f"theta2ArcCenterBot {arcs[0]["theta2"]}")
print (f"theta1ArcCenterUpperRight {arcs[1]["theta1"]}")
print (f"theta2ArcCenterUpperRight {arcs[1]["theta2"]}")
print (f"theta1ArcCenterUpperLeft {arcs[2]["theta1"]}")
print (f"theta2ArcCenterUpperLeft {arcs[2]["theta2"]}")

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')  # No axes

# Draw each arc
for arc in arcs:
    center_x, center_y = arc["center"]
    theta1 = arc["theta1"]
    theta2 = arc["theta2"]
    
    # Add the arc to the plot
    arc_patch = Arc(
        (center_x, center_y),  # Arc center
        width=2 * radius,  # Arc diameter
        height=2 * radius,  # Arc diameter
        angle=0,  # No rotation
        theta1=theta1,  # Start angle
        theta2=theta2,  # End angle
        edgecolor="black",
        linewidth=line_width, 
        capstyle='round'
    )
    ax.add_patch(arc_patch)

if includeCentralCircle:
    # Draw the central circle
    central_circle = plt.Circle(central_center, central_radius, edgecolor="black", fill=False, linewidth=line_width, capstyle='round')
    ax.add_artist(central_circle)

# Set limits for better visualization
ax.set_xlim(-2*radius, 4 * radius)
ax.set_ylim(-2*radius, 4 * radius)

# Save the figure
plt.savefig(output_file, format="png", dpi=300)
plt.close(fig)
'''
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(10)

triquetra_size = radius *2 #corners of a triangle that represents where each arc connects
#center = (0, -45) # I don't know why the default set this to -45 in y
center = (0, 0)
line_width = triquetra_size * 0.0866
circle_radius = triquetra_size * 0.7
triange_edge = math.sin(60)*triquetra_size
arc_radius = 2 * math.asin(60) * triquetra_size
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
    #radius is a = cos(60)*h
    arc(triquetra_size * 3**.5/2)
    t.right(60)
t.hideturtle()
screen.exitonclick()

# Save the drawing as a PostScript file
canvas = screen.getcanvas()
canvas.postscript(file="turtle_drawing.eps")

# Convert the PostScript file to PNG using Pillow
# This isn't working
img = Image.open("turtle_drawing.eps")
img.save("C:\\Users\\semic\\Python\\turtle_drawing.png", "png")

# Convert the canvas to a figure
# This isn't working
#fig = plt.figure()
#fig.canvas.draw()
#fig.canvas.blit(canvas.bbox)

# Save the figure as a PNG file
#plt.savefig("turtle_drawing.png")

# Convert to png with ghost script and os
# I get an error that 'gs' is not recognized as an internal or external command
#input_eps="turtle_drawing.eps"
#output_png="turtle_drawing.png"
#os.system(f"gswin64 -sDEVICE=pngalpha -o {output_png} -r300 {input_eps}")
'''