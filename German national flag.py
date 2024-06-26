import turtle


def draw_german_flag():
    """
 Function to draw the German flag using the turtle graphics library.

 The German flag consists of three horizontal stripes of equal width: black, red, and yellow.
 The flag is drawn with a ratio of 3:5, where the height is 3 units and the width is 5 units.

 Returns:
 - None

 """

    # Setting up the turtle screen and turtle object
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)  # Setting the screen size to match the flag ratio
    screen.title("German National Flag")
    screen.bgcolor("white")

    flag_turtle = turtle.Turtle()
    flag_turtle.speed(2)  # Setting the turtle speed to slow

    # Calculating the dimensions for the flag
    flag_width = 1000
    flag_height = 600

    flag_turtle.up()
    flag_turtle.goto(-100, -100)
    flag_turtle.down()

    # Yellow

    flag_turtle.color("yellow")
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

    # Red
    flag_turtle.color("red")
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

    # Black
    flag_turtle.color("black")
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
draw_german_flag()
