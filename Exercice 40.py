#!/usr/bin/env python
# coding: utf-8

# # Exercice 40

# In[5]:


import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        turtle.color("red")  # Couleur du premier côté
        turtle.forward(self.longueur)
        turtle.left(90)
        
        turtle.color("blue")  # Couleur du deuxième côté
        turtle.forward(self.largeur)
        turtle.left(90)
        
        turtle.color("green")  # Couleur du troisième côté
        turtle.forward(self.longueur)
        turtle.left(90)
        
        turtle.color("orange")  # Couleur du quatrième côté
        turtle.forward(self.largeur)
        turtle.left(90)

# Appel de la classe Rectangle
rectangle = Rectangle(200, 100)  # Création d'un rectangle avec longueur 200 et largeur 100

rectangle.tracer_figure()
turtle.done()


# In[ ]:





# In[ ]:




