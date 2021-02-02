#2-5
import turtle
sixsix=turtle.Turtle()
while True:

    l=int(input('要畫甚麼多邊形(3-oo)'))
    h=int(input('邊長為?'))
    g=360.0/l
    for k in range(l):
        sixsix.forward(h)
        sixsix.right(g)