# Author: SCT (AMDG) 3/18/22

# Import turtle
from cgitb import grey
import turtle

# Creates window
window = turtle.Screen()
window.setup(500, 500)
window.screensize(100,100)
window.title("Lab 3")
window.bgcolor("grey")

# Sets turtle name and color
ryan = turtle.Turtle()
ryan.shape("turtle")
ryan.pencolor("green")

# Directs turtle
for x in range(200):
    ryan.back(200)
    ryan.right(120)

# Keeps window open
window.mainloop()
