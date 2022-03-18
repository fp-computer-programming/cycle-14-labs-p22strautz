# Author: SCT (AMDG) 3/18/22

# Import turtle
from cgitb import grey
import turtle

# Creates window
window = turtle.Screen()
window.setup()
window.screensize()
window.title("Lab 4")
window.bgcolor("black")


# Sets turtle name and color
doug = turtle.Turtle()
doug.shape("turtle")
doug.pencolor("white")
doug.fillcolor("white")
doug.speed(5)
doug.stamp()
doug.setposition(100, 100)

# Directs turtle
doug.begin_fill()
doug.goto(100, 0)
doug.goto(0, 0)
doug.goto(0, 100)
doug.goto(100, 100)
doug.end_fill()

# Keeps window open
window.mainloop()
