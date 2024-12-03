import turtle


def draw_dutch_flag():
    """
 Function to draw the Dutch flag using the turtle graphics library.

 The Dutch flag consists of three horizontal stripes of equal width: blue, white, and red.
 The flag is drawn with a ratio of 3:5, where the height is 3 units and the width is 5 units.

 Returns:
 - None

 """

    # Setting up the turtle screen and turtle object
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)  # Setting the screen size to match the flag ratio
    screen.bgcolor("white")

    flag_turtle = turtle.Turtle()
    flag_turtle.speed(2)  # Setting the turtle speed to slow


    flag_turtle.up()
    flag_turtle.goto(-100, -100)
    flag_turtle.down()

    # Blue

    flag_turtle.color("blue")
    flag_turtle.begin_fill()
    flag_turtle.forward(200)
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.left(90)
    flag_turtle.forward(200)
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.end_fill()

    # Move for next color

    flag_turtle.up()
    flag_turtle.goto(100, -50)
    flag_turtle.down()

    # White
    flag_turtle.color("white")
    flag_turtle.begin_fill()
    flag_turtle.left(90)
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.left(90)
    flag_turtle.forward(200)
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.left(90)
    flag_turtle.forward(200)
    flag_turtle.end_fill()

    # Move for next color
    flag_turtle.up()

    flag_turtle.goto(100, 0)

    flag_turtle.down()

    # Red
    flag_turtle.color("red")
    flag_turtle.begin_fill()
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.left(90)
    flag_turtle.forward(200)
    flag_turtle.left(90)
    flag_turtle.forward(50)
    flag_turtle.left(90)
    flag_turtle.forward(200)
    flag_turtle.end_fill()

    flag_turtle.hideturtle()

    while True:
     screen.update()

# Calling the function to draw the German flag
draw_dutch_flag()
