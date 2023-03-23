import logging
import turtle

logging_level = logging.DEBUG

def draw_eq_tri(turtle, side_length, start_heading, start_x, start_y, color, fill):
    pass

def draw_rect(turtle, length, width, start_x, start_y, color, fill):
    """Draws a rectangle.
turtle [turtle.Turtle] - turtle to draw rectangle with
length [int/float] - length (north-south) of rectangle
width [int/float] - width (west-east) of rectangle
start_x, start_y [int/float] - start position (bottom left corner)
color [str] - Tk colour specification string of color of rectangle
fill [bool] - option to fill rectangle (if True)
Note: turtle will end with heading 90 (north)"""

    logging.debug(f"draw_rect called with arguments turtle={turtle}, length={length}, width={width}, start_x={start_x}, start_y={start_y}, color={color}, fill={fill}")
    turtle.pu()
    turtle.goto(start_x, start_y)
    turtle.pd()
    
    turtle.seth(90)
    turtle.color(color)
    
    if fill:
        turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)

    turtle.end_fill()
        
    
def draw_frame(turtle):
    """Draws a frame for a picture."""

    draw_rect(turtle, 400, 400, -200, -200, "black", False)

t = turtle.Turtle()
draw_frame(t)
