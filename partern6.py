import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw(length=100, degree=144):
  t.forward(length)
  t.right(degree)

for _ in range(5):
  draw()

screen.exitonclick()
