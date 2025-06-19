'''
Turtle Graphics - Concentric Circles
Author: Alexandr Iapara
Description: Utility functions to draw concentric circles using the turtle graphics module.
'''

# Import Turtle graphics module
import turtle
t = turtle.Turtle()

def move(t, x, y):
   """
   Move Turtle to x, y position

   This function lifts the pen, moves the turtle to the specified (x, y) coordinates,
   and then puts the pen down to resume drawing.

   Args:
      t (Turtle): The turtle object used for drawing.
      x (int or float): The x-coordinate to move to.
      y (int or float): The y-coordinate to move to.

   Returns:
      None
   """
   t.pu()
   t.goto(x, y)
   t.pd()
   
def draw_circle(t, radius, x, y):
   """
   Draws a circle with the specified radius using the given Turtle object, centered at (x, y).

   The function moves the turtle to the correct starting position so that the circle is centered at (x, y), then draws the circle.

   Args:
      t (turtle.Turtle): The Turtle object used to draw the circle.
      radius (float): The radius of the circle to be drawn.
      x (float): The x-coordinate of the center of the circle.
      y (float): The y-coordinate of the center of the circle.

   Returns:
      None
   """
   move(t, x, y - radius)
   t.circle(radius)
   
def draw_concentric_circles(t, circles, radius, gap, x, y):
   """
   Draws a series of concentric circles using the specified Turtle object.

   Args:
      t (turtle.Turtle): The Turtle object used for drawing.
      circles (int): The number of concentric circles to draw.
      radius (float): The initial radius of the circles.
      gap (float): The gap between each circle.
      x (float): The x-coordinate of the center of the circles.
      y (float): The y-coordinate of the center of the circles.

   Returns:
      None
   """
   for i in range(circles):
      draw_circle(t, radius, x, y)
      radius = radius + gap

draw_concentric_circles(t, 3, 50, 25, 0, 0)
