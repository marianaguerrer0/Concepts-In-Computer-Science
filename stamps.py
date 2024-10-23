# Mariana Guerrero
# Travel Stamps
# COP 2500C
# July 19, 2024


import turtle

#Defining function.
#First stamp, sunflower: I picked this flower since it has been a representation of my family
#over the years.Sunflowers have been around me growing up until this day.
#Defining function.
def marianaguerrero_entry(x,y,scale):
    turtle.penup()
    turtle.goto(-200,-31)
    turtle.pendown()

    turtle.speed(200)
    
    #First circle, green.
    turtle.fillcolor("#c2f0d8")
    turtle.begin_fill()

    turtle.circle(58*scale,360)

    turtle.end_fill()

    turtle.penup()
    turtle.goto(-200,-8)
    turtle.pendown()

    #Second circle, yellow.
    turtle.fillcolor("#fce76d")
    turtle.begin_fill()

    turtle.circle(45*scale,360)

    turtle.end_fill()
    
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(90)
    turtle.pendown()

    #Start flower.
    turtle.fillcolor("#f0a729")
    turtle.begin_fill()
    
    for i in range(20):
        turtle.circle(48*scale,45)
        turtle.left(90)
        turtle.circle(48*scale,45)
        turtle.left(18)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(4)
    turtle.pendown()
    
    turtle.fillcolor("#524033")
    turtle.begin_fill()
    turtle.circle(14*scale,360)
    turtle.end_fill()

# Second stamp, Colombian Flag: I decided to pick the flag as a representation of my country
# of origin.
def marianaguerrero_exit(x,y,scale):
    turtle.penup()
    turtle.goto(98*scale,10)
    turtle.pendown()

    #First circle: green.
    turtle.fillcolor("#c2f0d8")
    turtle.begin_fill()

    turtle.circle(58*scale,360)

    turtle.end_fill()
    
    turtle.penup()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(90)
    turtle.pendown()

    turtle.penup()
    turtle.goto(136,60)
    turtle.pendown()

    #First rectangle: yellow.
    turtle.fillcolor("#f5ea4c")
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(110)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()

    #Second rectangle: blue.
    turtle.fillcolor("#1b7df5")
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(110)
        turtle.right(90)
    turtle.end_fill()


    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

    #Third rectangle: red.
    turtle.fillcolor("#f52f38")
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(110)
        turtle.right(90)
    turtle.end_fill()

def main():

    marianaguerrero_entry(-20,0,2)
    marianaguerrero_exit(20,0,2)

main()

