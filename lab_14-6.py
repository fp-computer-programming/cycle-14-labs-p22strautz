# Author: SCT (AMDG) 3/23/22

# imports turtles plugin
import turtle

# creates window
window = turtle.Screen()

# creates turtle
john = turtle.Turtle()

# text intupts for color and size
john.color(window.textinput("Color?", "What color would you like?"))
size = int(window.textinput("Size?", "What size would you like the turtle to be (1-5)?"))

# creates size based on decison
if size > 5:
    john.shapesize(5)
elif size < 1:
    john.shapesize(1)
else:
    john.shapesize(size)

# movements for turtle that is created
john.begin_fill()
john.forward(100)
john.right(90)
john.forward(100)
john.right(90)
john.forward(100)
john.right(90)
john.forward(100)
john.end_fill()

# keeps window open
window.listen()
window.mainloop()