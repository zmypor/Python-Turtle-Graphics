import turtle


def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    whiterectangle(t, -190, 100, 380, 200)
    strip(t, -190, 100, 380, 200)
    bluerectangle(t, -190, 100, 380, 200)
    stars(t, -190, 100, 380, 200)


def whiterectangle(t, x, y, w, h):
    t.color('white', 'white')
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.down()
    t.goto(x + w, y)
    t.goto(x + w, y - h)
    t.goto(x, y - h)
    t.goto(x, y)
    t.end_fill()
    t.up()


def strip(t, x, y, w, h):
    for i in range(7):
        t.up()
        t.goto(x, y - 2 * (h / 13) * i)
        t.down()
        t.color('red', 'red')
        t.begin_fill()
        t.goto(x + w, y - 2 * (h / 13) * i)
        t.goto(x + w, y - 2 * (h / 13) * i - (h / 13))
        t.goto(x, y - 2 * (h / 13) * i - (h / 13))
        t.goto(x, y - 2 * (h / 13) * i)
        t.end_fill()
        t.up()


def bluerectangle(t, x, y, w, h):
    t.color('blue', 'blue')
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.down()
    t.goto(x + .4 * w, y)
    t.goto(x + .4 * w, y - (7 / 13) * h)
    t.goto(x, y - (7 / 13) * h)
    t.goto(x, y)
    t.end_fill()


def star(t, x1, y1):
    t.up()
    t.goto(x1, y1)
    t.left(36)
    t.down()
    t.fillcolor('white')
    t.begin_fill()
    for i in range(5):
        t.pencolor('white')
        t.forward(8.4)
        t.left(144)
    t.end_fill()
    t.right(36)


def stars(t, x, y, w, h):
    t.up()
    for i in range(5):
        for j in range(6):
            t.up()
            t.down()
            star(t, x + (1 / 18) * w * .4 + j * (1 / 6) * w * .4,\
            y - (2 / 11) * (7 / 13) * h - 2 * i * (1 / 11) * (7 / 13) * h)
    for i in range(4):
        for j in range(5):
            t.up()
            t.down()
            star(t, x + (2 / 17) * w * .4 + j * (3 / 17) * w * .4,\
            y - (3 / 11) * (7 / 13) * h - 2 * i * (1 / 11) * (7 / 13) * h)


main()
turtle.done()