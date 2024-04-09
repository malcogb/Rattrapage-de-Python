#!/usr/bin/env python
# coding: utf-8

# # Exercice 42

# In[8]:


from math import gcd

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def invert(self):
        return Fraction(self.denominateur, self.numerateur)

    def simplify(self):
        common_divisor = gcd(self.numerateur, self.denominateur)
        return Fraction(self.numerateur // common_divisor, self.denominateur // common_divisor)

    def __mul__(self, other):
        return Fraction(self.numerateur * other.numerateur, self.denominateur * other.denominateur)

    def __add__(self, other):
        new_numerateur = self.numerateur * other.denominateur + other.numerateur * self.denominateur
        new_denominateur = self.denominateur * other.denominateur
        return Fraction(new_numerateur, new_denominateur)

    def __sub__(self, other):
        new_numerateur = self.numerateur * other.denominateur - other.numerateur * self.denominateur
        new_denominateur = self.denominateur * other.denominateur
        return Fraction(new_numerateur, new_denominateur)

    def __truediv__(self, other):
        return self * other.invert()

    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"

    @classmethod
    def from_string(cls, string):
        numerateur, denominateur = map(int, string.split('/'))
        return cls(numerateur, denominateur)

# Exemple d'utilisation de la classe Fraction
f1= Fraction(2,4)
f2 =Fraction(1,4)
f3= f1+f2
f4= f1-f2
f5= f1*f2
f6= f1/f2
f7= Fraction(4,10)
f8 = Fraction.from_string('5/10')

print("f1:", f1)
print("f2:", f2)


print("f3:", f3.simplify()) # affiche: 3/4
print("f4:", f4.simplify()) # affiche: 1/4
print("f5:", f5.simplify()) # affiche: 1/8
print("f6:", f6.simplify()) # affiche: 2
print("f7 simplifiée:", f7.simplify()) # affiche: 2/5
print("f7 inversée:", f7.invert()) # affiche: 10/4
print("f8 :", f8) # affiche: 5/10




# In[ ]:




