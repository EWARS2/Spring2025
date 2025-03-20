"""
Program #5: Line Spirograph
Write a program that creates some interesting "spirograph" pattern based upon
repeatedly printing out lines.
Use one or more "for loops" to accomplish this.
"""
import turtle

bob = turtle.Turtle()
bob.speed(0)

bob.pendown()
for i in range(100):
    bob.forward(200)
    bob.right(91)

turtle.done()
