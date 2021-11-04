import turtle
import random
from random import randrange,uniform

t = turtle.Turtle()
a=randrange(10,200)
b=randrange(10,200)
def stvorec():
    t.penup()
    prvapoz = random.randrange(-300,300)
    druhapoz = random.randrange(-300,300)
    t.pencolor("red")
    t.setposition(prvapoz,druhapoz)
    t.pendown()
    for i in range(4):
        t.forward(a)
        t.right(90)
def trojuholnik():
    t.penup()
    prvapoz = random.randrange(-300,300)
    druhapoz = random.randrange(-300,300)
    t.pencolor("blue")
    t.setposition(prvapoz,druhapoz)
    t.pendown()
    for i in range(3):
        t.forward(b)
        t.right(120)

pocettroj=random.randrange(1,10)
pocetstvor=random.randrange(1,10)

for y in range(pocettroj):
    stvorec()
    trojuholnik()

turtle.exitonclick()

t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.left(20)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.left(20)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.forward(60)
t.left(90)
t.left(20)

t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)
t.forward(60)
t.left(90)
t.forward(60)
t.right(90)

def prvacast():
    for i in range(6):
        t.forward(60)
        t.right(60)
prvacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.right(60)
druhacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.left(60)
druhacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.left(60)
druhacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.left(60)
druhacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.left(60)
druhacast()
t.left(120)
def druhacast():
    for i in range(5):
        t.forward(60)
        t.left(60)
druhacast()

