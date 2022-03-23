# Author: SCT (AMDG) 3/23/22

# import turtles plugin
import turtle

# defines rotations and movement function
def move_forward():
    john.forward(50)

def move_backward():
    john.backward(50)

def turn_left():
    john.left(90)

def turn_right():
    john.right(90)

# creates window
window = turtle.Screen()

# creates turtle
john = turtle.Turtle()

# sets movements to keys
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

# keeps window open
window.listen()
window.mainloop()