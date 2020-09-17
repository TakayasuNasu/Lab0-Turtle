import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
lenght = 100
angle = -60
def exercise_4():
    for i in range(6):
        t.forward(lenght)
        t.setheading(angle*(i+1))
    t.setheading(angle)
    t.forward(2*lenght)
    t.setheading(-3*angle)
    t.up()
    t.forward(lenght)
    t.setheading(-1*angle)
    t.down()
    t.forward(2*lenght)
    t.up()
    t.setheading(angle)
    t.forward(lenght)
    t.setheading(3 * angle)
    t.down()
    t.forward(2 * lenght)
    screen.exitonclick()
exercise_4()