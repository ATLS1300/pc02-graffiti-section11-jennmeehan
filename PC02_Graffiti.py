#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Jenn Meehan
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.speed(0)

turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(125)
turtle.end_fill()

turtle.up()
turtle.goto(-50, 140)
turtle. down()
turtle.begin_fill()
turtle.fillcolor("white")
turtle.circle(30)
turtle.end_fill()

turtle.up()
turtle.goto(50, 140)
turtle.down()
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.up()
turtle.goto(-60, 165)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(15)
turtle.end_fill()

turtle.up()
turtle.goto(40, 165)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(15)
turtle.end_fill()

turtle.up()
turtle.goto(45, 70)
turtle.down()
turtle.begin_fill()
turtle.goto(10,95)
turtle.goto(-10, 95)
turtle.goto(-45, 70)
turtle.goto(-10, 82)
turtle.goto(10, 82)
turtle.goto(45, 70)
turtle.end_fill()

turtle.up()
turtle.goto(-270, 200)
turtle.pensize(2)
turtle.setheading(45)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("gray")
turtle.forward(125)
turtle.setheading(135)
turtle.forward(50)
turtle.setheading(45)
turtle.backward(125)
turtle.setheading(135)
turtle.backward(50)
turtle.end_fill()

turtle.up()
turtle.forward(25)
turtle.down()
turtle.pensize(4)
turtle.setheading(45)
turtle.color("red")
turtle.backward(25)
turtle.forward(50)

turtle.up()
turtle.setheading(135)
turtle.forward(25)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.setheading(10)
turtle.backward(20)
turtle.forward(20)
turtle.setheading(45)
turtle.backward(50)
turtle.setheading(63.842)
turtle.forward(35.52)
turtle.end_fill()

turtle.up()
turtle.goto(-270, 200)
turtle.setheading(45)
turtle.forward(25)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.setheading(800)
turtle.backward(20)
turtle.forward(20)
turtle.setheading(45)
turtle.backward(50)
turtle.setheading(26.158)
turtle.forward(35.52)
turtle.end_fill()

turtle.up()
turtle.goto(-270, 200)
turtle.setheading(45)
turtle.forward(125)
turtle.setheading(135)
turtle.backward(10)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.setheading(85)
turtle.forward(54.45)
turtle.backward(54.45)
turtle.setheading(135)
turtle.forward(70)
turtle.setheading(5)
turtle.forward(54.45)
turtle.end_fill()

turtle.up()
turtle.setheading(45)
turtle.backward(60)
turtle.setheading(135)
turtle.pensize(2)
turtle.color("black")
turtle.down()
turtle.begin_fill()
turtle.fillcolor("lightblue")
turtle.circle(15)
turtle.end_fill()

turtle.up()
turtle.goto(-100, -300)
turtle.write("Is that my spaceship?", font = 100)


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
