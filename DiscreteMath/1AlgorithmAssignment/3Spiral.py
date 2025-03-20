"""
Program #3: Spiral Write a program to draw the following pattern.
"""
import turtle

bob = turtle.Turtle()
bob.speed(0)
page = turtle.Screen()
page.bgcolor("white")
bob.color("blue")

bob.pendown()
for i in range(50, 1000, 2):
    bob.forward(i)
    bob.right(91)

turtle.done()
