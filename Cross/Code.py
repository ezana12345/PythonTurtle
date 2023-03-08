import turtle

t = turtle.Turtle()
t.color("Red")
t.begin_fill()

for x in range(4):
  t.rt(90)
  t.fd(100)
  t.lt(90)
  t.fd(50)
  t.lt(90)
  t.fd(100)
t.end_fill()
