# Import Turtle graphics module 
import turtle
t = turtle.Turtle()

def draw_line(t, x, y, angle, length):
    """
    Draws a straight line starting from (x, y) at a specified angle and length using the given Turtle.

    The function lifts the pen to move the turtle to the starting coordinates (x, y) without drawing.
    It then sets the turtle's heading to the specified angle (in degrees), puts the pen down, and draws a line forward by the given length.
    After drawing, the pen is lifted again to avoid drawing unintended lines when moving the turtle elsewhere.

    Args:
        t (Turtle): The turtle object used for drawing.
        x (int or float): The starting x-coordinate.
        y (int or float): The starting y-coordinate.
        angle (int or float): The angle (in degrees) at which to draw the line.
        length (int or float): The length of the line to draw.

    Returns:
        None
    """
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()

#draw_line(t, 0, 0, 45, 80)
#draw_line(t, -100, 50, 90, 120)
#draw_line(t, 60, -80, 180, 60)

def draw_radial_lines(t, x, y, length, num_lines):
    """
    Draws multiple lines (radials) originating from a common point, evenly spaced around a full circle.

    The function calculates the angle between each line by dividing 360 degrees by the number of lines.
    It then iterates through the number of lines, drawing each line from the starting point (x, y) at the appropriate angle,
    resulting in lines radiating outward like spokes on a wheel.

    Args:
        t (Turtle): The turtle object used for drawing.
        x (int or float): The starting x-coordinate for the center of the radials.
        y (int or float): The starting y-coordinate for the center of the radials.
        length (int or float): The length of each radial line.
        num_lines (int): The number of radial lines to draw.

    Returns:
        None
    """
    angle = 360 / num_lines
    for i in range(num_lines):
        draw_line(t, x, y, i * angle, length)
        
#draw_radial_lines(t, 0, 0, 50, 6)
#draw_radial_lines(t, 100, 100, 30, 12)
#draw_radial_lines(t, -100, 50, 70, 5)