# Author: SCT (AMDG) 3/17/22

# Import turtle
import turtle

# Creates window
window = turtle.Screen()
window.setup(1000, 1000)
window.screensize(100,100)
window.title("Lab 1")

# Sets turtle name
pierre = turtle.Turtle()

# Directs turtle
pierre.forward(250)
pierre.right(90)
pierre.forward(100)
pierre.right(90)
pierre.forward(250)
pierre.right(90)
pierre.forward(100)

# Keeps window open
window.mainloop()
