import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to the fastest

# Draw a heart
t.color('red')
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
