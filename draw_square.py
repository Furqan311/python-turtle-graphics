import turtle as g;

g.setup(width=200, height=300, startx=1, starty=1)
g.title("Text To bew Displasyed")
g.pencolor('red')

g.forward(50) #it will move the cursor forward by the specified distance
g.right(90)     #it will turn the cursor right by angle units
g.forward(50)
g.right(90)
g.forward(50)
g.right(90)
g.forward(50)
g.right(90)
g.hideturtle()    #it will hide the red cursor after the image has been rendered completely
g.exitonclick();  #it will close the window when it is clicked anywhere inside the window area

#Optional Functions are
#left(angle) It turn the cursor by angle units.
#setheading(to_angle) It sets the heading of the cursor to the specified aangle
#backward(distance) It move the cursoor backward by the specified length from the current position

#goto(x, y) It will move the cursor directly the specified coordinated
# set(x) or set(y) used to move the cursor to x or y location implicitly.