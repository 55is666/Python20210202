#2-4
import turtle,random
h=random.randint(1,100)
j=random.randint(1,360)
fourfour = turtle.Turtle()
fourfour.color('blue')
while True:
    fourfour.forward(h)
    fourfour.left(j)
    h=random.randint(1,100)
    j=random.randint(1,360)
    fourfour.forward(h)
    fourfour.right(j)
    h=random.randint(1,100)
    j=random.randint(1,360)