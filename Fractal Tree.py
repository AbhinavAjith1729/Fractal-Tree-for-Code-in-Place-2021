# Fractal Tree using Turtle by Abhinav Ajith

import turtle as tu

littlemice = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("black")  # Screen Bg color
wn.title("Fractal Tree Pattern")
littlemice.left(90)  # moving the turtle 90 degrees towards left
littlemice.speed(10000)  # setting the speed of the turtle


def draw(l):  # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:

        littlemice.pensize(2)  # Setting Pensize
        littlemice.pencolor("yellow")  # Setting Pencolor as yellow
        littlemice.forward(l)  # moving turtle forward by 'l'
        littlemice.left(30)  # moving the turtle 30 degrees towards left
        draw(3 * l / 4)  # drawing a fractal on the left of the turtle object 'littlemice' with 3/4th of its length
        littlemice.right(60)  # moving the turtle 60 degrees towards right
        draw(3 * l / 4)  # drawing a fractal on the right of the turtle object 'littlemice' with 3/4th of its length
        littlemice.left(30)  # moving the turtle 30 degrees towards left
        littlemice.pensize(2)
        littlemice.backward(l)  # returning the turtle back to its original psition


draw(20)  # drawing 20 times

littlemice.right(90)
littlemice.speed(10000)


# recursion of same process
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor("magenta")  # magenta
        littlemice.forward(l)
        littlemice.left(30)
        draw(3 * l / 4)
        littlemice.right(60)
        draw(3 * l / 4)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(20)

littlemice.left(270)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor("red")  # red
        littlemice.forward(l)
        littlemice.left(30)
        draw(3 * l / 4)
        littlemice.right(60)
        draw(3 * l / 4)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(20)

littlemice.right(90)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor('#FFF8DC')  # white
        littlemice.forward(l)
        littlemice.left(30)
        draw(3 * l / 4)
        littlemice.right(60)
        draw(3 * l / 4)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(20)


def draw(l):
    if (l < 10):
        return
    else:

        littlemice.pensize(3)
        littlemice.pencolor("lightgreen")  # lightgreen
        littlemice.forward(l)
        littlemice.left(30)
        draw(4 * l / 5)
        littlemice.right(60)
        draw(4 * l / 5)
        littlemice.left(30)
        littlemice.pensize(3)
        littlemice.backward(l)


draw(40)

littlemice.right(90)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(3)
        littlemice.pencolor("red")  # red
        littlemice.forward(l)
        littlemice.left(30)
        draw(4 * l / 5)
        littlemice.right(60)
        draw(4 * l / 5)
        littlemice.left(30)
        littlemice.pensize(3)
        littlemice.backward(l)


draw(40)

littlemice.left(270)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(3)
        littlemice.pencolor("yellow")  # yellow
        littlemice.forward(l)
        littlemice.left(30)
        draw(4 * l / 5)
        littlemice.right(60)
        draw(4 * l / 5)
        littlemice.left(30)
        littlemice.pensize(3)
        littlemice.backward(l)


draw(40)

littlemice.right(90)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(3)
        littlemice.pencolor('#FFF8DC')  # white
        littlemice.forward(l)
        littlemice.left(30)
        draw(4 * l / 5)
        littlemice.right(60)
        draw(4 * l / 5)
        littlemice.left(30)
        littlemice.pensize(3)
        littlemice.backward(l)


draw(40)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        littlemice.pensize(2)
        littlemice.pencolor("cyan")  # cyan
        littlemice.forward(l)
        littlemice.left(30)
        draw(6 * l / 7)
        littlemice.right(60)
        draw(6 * l / 7)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(60)

littlemice.right(90)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor("yellow")  # yellow
        littlemice.forward(l)
        littlemice.left(30)
        draw(6 * l / 7)
        littlemice.right(60)
        draw(6 * l / 7)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(60)

littlemice.left(270)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor("magenta")  # magenta
        littlemice.forward(l)
        littlemice.left(30)
        draw(6 * l / 7)
        littlemice.right(60)
        draw(6 * l / 7)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(60)

littlemice.right(90)
littlemice.speed(10000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        littlemice.pensize(2)
        littlemice.pencolor('#FFF8DC')  # white
        littlemice.forward(l)
        littlemice.left(30)
        draw(6 * l / 7)
        littlemice.right(60)
        draw(6 * l / 7)
        littlemice.left(30)
        littlemice.pensize(2)
        littlemice.backward(l)


draw(60)
wn.exitonclick()
