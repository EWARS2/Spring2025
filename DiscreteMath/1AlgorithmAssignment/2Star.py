"""
Program #2: Star
Write a program to draw the following shape.
Make sure you use a for loop.
"""
import turtle

size = 100

bob = turtle.Turtle()
bob.speed(0)
page = turtle.Screen()
page.bgcolor("white")
bob.color("blue")

bob.pendown()
for side in range(5):
    bob.forward(size)
    bob.right(144)
    bob.forward(size)
    bob.left(72)

turtle.done()
