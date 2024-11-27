# Drawing flags usiong Python Turtle
import turtle

flag_turtle = turtle.Turtle()
flag_turtle.shape("arrow")
flag_turtle.speed(1)

window = turtle.Screen()
window.bgcolor("#DDDDDD")

# Draw the frame for the flag
flag_turtle.color("white")
flag_turtle.pensize(2)
flag_turtle.fillcolor("white")
# Position the pen in the bottom left corner
flag_turtle.penup()
flag_turtle.goto(-180, -120)
flag_turtle.pendown()
flag_turtle.begin_fill()
flag_turtle.goto(180, -120)
flag_turtle.goto(180, 120)
flag_turtle.goto(-180, 120)
flag_turtle.goto(-180, -120)
flag_turtle.end_fill()

# Draw the blue stripe
flag_turtle.color("blue")
flag_turtle.pensize(2)
flag_turtle.fillcolor("blue")

flag_turtle.penup()
flag_turtle.goto(-180, -120)
flag_turtle.pendown()
flag_turtle.begin_fill()
flag_turtle.goto(-60, -120)
flag_turtle.goto(-60, 120)
flag_turtle.goto(-180, 120)
flag_turtle.goto(-180, -120)
flag_turtle.end_fill()

# Draw the red stripe
flag_turtle.color("red")
flag_turtle.pensize(2)
flag_turtle.fillcolor("red")

flag_turtle.penup()
flag_turtle.goto(60, -120)
flag_turtle.pendown()
flag_turtle.begin_fill()
flag_turtle.goto(180, -120)
flag_turtle.goto(180, 120)
flag_turtle.goto(60, 120)
flag_turtle.goto(60, -120)
flag_turtle.end_fill()

# Adding Text...
flag_turtle.penup()
flag_turtle.goto(-62, -160)
flag_turtle.color("white")
flag_turtle.write("FRANCE", None, None, "24pt bold")

# 维持面板
while True:
    screen.update()
    turtle.done()