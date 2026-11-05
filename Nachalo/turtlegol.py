import turtle as t

r = input("Ведите радиус")
t.colormode(255)
for i in range(3):
    t.begin_fill()
    t.color(255, 127, 80)
    t.circle(r)
    t.end_fill()
    t.penup()
    t.fd(50)
    t.pendown()

