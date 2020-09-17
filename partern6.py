import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

def draw(lenght=100, digree=144):
  t.forward(lenght)
  t.right(digree)

for _ in range(5):
  draw()

screen.exitonclick()