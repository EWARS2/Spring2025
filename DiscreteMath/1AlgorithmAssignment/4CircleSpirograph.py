"""
Program #4: Circle Spirograph
Write a program that creates some interesting "spirograph" pattern based upon
repeatedly printing out circles.
Use one or more "for loops" to accomplish this.
"""
import turtle

bob = turtle.Turtle()
bob.speed(0)

for i in range(100):
    bob.circle(100)
    bob.right(91)

turtle.done()