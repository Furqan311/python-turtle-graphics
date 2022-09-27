import turtle as turtle;

def initiateWindow():
    turtle.setup(width=500, height=600, startx=1, starty=1)
    turtle.title("Text To bew Displasyed")
    turtle.exitonclick()


def emptyCircle():
    initiateWindow()
    turtle.pencolor('red')
    turtle.circle(radius=100)

emptyCircle()

def filledcircle():
    turtle.dot(100, "red")

filledcircle()