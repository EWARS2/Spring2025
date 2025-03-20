"""
Program #2: Star
Write a program to draw the following shape.
Make sure you use a for loop.
"""

# Based on sample code from Moodle
import turtle
import random
bob = turtle.Turtle()
bob.speed(0)
page = turtle.Screen()
page.bgcolor("black")
bob.color("yellow")
for star in range(100):
  x = random.randint(0,100)
  y = random.randint(0,360)
  bob.penup()
  bob.right(y)
  bob.forward(x)
  bob.pendown()
  bob.begin_fill()
  for side in range(5):
    bob.forward(10)
    bob.right(144)
  bob.end_fill()

