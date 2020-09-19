# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:37:11 2020

@author: Elève
"""


import turtle


def von_koch(n: int, segment: int) -> None:
    if n > 0:
        von_koch(n - 1, segment / 3)
        turtle.left(60)
        von_koch(n - 1, segment / 3)
        turtle.right(120)
        von_koch(n - 1, segment / 3)
        turtle.left(60)
        von_koch(n - 1, segment / 3)
    else:
        turtle.forward(segment)


def flocon_koch(n: int, segment: int) -> None:
    if n == 0:
        turtle.forward(segment)
    else:
        von_koch(n, segment / 3)
        turtle.right(120)
        von_koch(n, segment / 3)
        turtle.right(120)
        von_koch(n, segment / 3)
        turtle.right(120)


def turtle_init() -> None:
    # turtle init
    turtle.home()
    turtle.clear()
    turtle.showturtle()
    turtle.hideturtle()
    turtle.color("blue")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.speed(0)
    
a = turtle.Screen()
a.screensize(10_000, 6_000)
turtle_init()
flocon_koch(8, 10_000)
turtle.done()