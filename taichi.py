import turtle

t = turtle.Turtle()

t.pencolor('black')
t.pensize(2)
t.end_fill()

# left part
t.fillcolor('white')
t.begin_fill()
t.circle(100, 180)
t.circle(200, 180)
t.circle(100, -180)
t.end_fill()
# right part
t.fillcolor('black')
t.begin_fill()
t.circle(100, 180)
t.circle(200, 180)
t.circle(100, -180)
t.penup()
# black dot
t.lt(90)
t.forward(100)
t.end_fill()
t.dot(45)
t.pendown()
# white dot
t.penup()
t.rt(90)
t.rt(90)
t.forward(200)
t.pencolor('white')
t.pendown()
t.dot(45)
t.penup()
t.forward(190)

t.pencolor("black")
t.write('Tawheed', font=("Ani", 30, "bold"))
t.hideturtle()
turtle.done()
