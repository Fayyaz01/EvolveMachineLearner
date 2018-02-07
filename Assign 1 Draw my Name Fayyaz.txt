# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from turtle import Turtle, Screen


class Draw_My_Name:
    NAME = "FAYYAZ"

    BORDER = 1
    BOX_WIDTH, BOX_HEIGHT = 6, 10  # letter bounding box
    WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size
    
    def letter_A(self, turtle):
        turtle.forward(self.HEIGHT / 2)
        for _ in range(3):
            turtle.forward(self.HEIGHT / 2)
            turtle.right(90)
            turtle.forward(self.WIDTH)
            turtle.right(90)
        turtle.forward(self.HEIGHT)
    
    def letter_D(self, turtle):
        turtle.forward(self.HEIGHT)
        turtle.right(90)
        turtle.circle(-self.HEIGHT / 2, 180, 30)
    
    def letter_I(self, turtle):
        turtle.right(90)
        turtle.forward(self.WIDTH)
        turtle.backward(self.WIDTH / 2)
        turtle.left(90)
        turtle.forward(self.HEIGHT)
        turtle.right(90)
        turtle.backward(self.WIDTH / 2)
        turtle.forward(self.WIDTH)
    
    def letter_N(self, turtle):
        turtle.forward(self.HEIGHT)
        turtle.goto(turtle.xcor() + self.WIDTH, self.BORDER)
        turtle.forward(self.HEIGHT)
    
    
    def letter_F(self, turtle):
        turtle.forward(self.HEIGHT / 2)
        turtle.right(90)
        turtle.forward(self.WIDTH)
        turtle.backward(self.WIDTH)
        turtle.left(90)
        turtle.forward(self.HEIGHT / 2)
        turtle.right(90)
        turtle.forward(self.WIDTH)
        turtle.backward(self.WIDTH)
        turtle.left(90)
        
        
    def letter_Y(self, turtle):
        turtle.pencolor("white")
        turtle.right(90)
        turtle.forward(self.WIDTH / 2)
        turtle.left(90)
        turtle.pencolor("black")
        turtle.forward(self.HEIGHT / 2)
        turtle.right(90)
        turtle.forward(self.WIDTH / 2)
        turtle.left(90)
        turtle.forward(self.WIDTH)
        turtle.backward(self.WIDTH)
        turtle.left(90)
        turtle.forward(self.WIDTH)
        turtle.right(90)
        turtle.forward(self.WIDTH)
    
    def letter_Z(self, turtle):
        turtle.pencolor("white")
        turtle.forward(self.HEIGHT)
        turtle.right(90)
        turtle.pencolor("black")
        turtle.forward(self.WIDTH)
        turtle.goto(turtle.xcor() - self.WIDTH, self.BORDER )
        turtle.forward(self.WIDTH)
    
    #LETTERS = {'A': letter_A, 'D': letter_D, 'I': letter_I, 'N': letter_N}
    LETTERS = {'F': letter_F , 'A': letter_A , 'Y' : letter_Y , 'Z' : letter_Z}    
    wn = Screen()
    def __init__(self):
    
        self.wn.setup(800, 400)  # arbitrary
        self.wn.title("Turtle writing my name: {}".format(self.NAME))
        self.wn.setworldcoordinates(0, 0, self.BOX_WIDTH * len(self.NAME), self.BOX_HEIGHT)
    
        marker = Turtle()
        
        for counter, letter in enumerate(self.NAME):
            marker.penup()
            marker.goto(counter * self.BOX_WIDTH + self.BORDER, self.BORDER)
            marker.setheading(90)
        
            if letter in self.LETTERS:
                marker.pendown()
                self.LETTERS[letter](self, marker)
        
        #marker.hideturtle()
        
        self.wn.mainloop()



Fayyaz = Draw_My_Name()