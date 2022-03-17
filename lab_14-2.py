# Author: SCT (AMDG) 3/17/22

import turtle # Import turtle

# Creates window
window = turtle.Screen()
window.setup(500, 500)
window.screensize(100,100)
window.title("Lab 2")

# Sets name of turtle
frog = turtle.Turtle()

# Directs the turtle
frog.forward(100)
frog.right(120)
frog.forward(100)
frog.right(120)
frog.forward(100)

# Keeps window open
window.mainloop()
