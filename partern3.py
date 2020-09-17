import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
def draw_square(lenght: int):
    for i in range(4):
        t.forward(lenght)
        t.right(90)
def exercise_3():
    draw_square(100)
    t.up()
    t.goto(50, 50)
    t.down()
    draw_square(100)
    screen.exitonclick()
exercise_3()