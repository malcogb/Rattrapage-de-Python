#!/usr/bin/env python
# coding: utf-8

# # Exercice 43

# In[3]:


import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw_rect(self):
        turtle.fillcolor("white")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.longueur)
            turtle.right(90)
            turtle.forward(self.largeur)
            turtle.right(90)
        turtle.end_fill()

class Square(Rectangle):
    def __init__(self, cote, inclinaison_initiale=30):
        super().__init__(cote, cote)
        self.inclinaison_initiale = inclinaison_initiale

    def draw_squ(self):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.right(self.inclinaison_initiale)
        for _ in range(4):
            turtle.forward(self.longueur)
            turtle.right(90)
        turtle.end_fill()

# Appel des classes rectangle et square
rectangle = Rectangle(200, 100)
rectangle.draw_rect()

turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

square = Square(150)
square.draw_squ()

turtle.done()

