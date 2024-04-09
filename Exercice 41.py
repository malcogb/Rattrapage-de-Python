#!/usr/bin/env python
# coding: utf-8

# # Exercice 41

# In[2]:


from collections import UserString

class MyString(UserString):
    def head(self, n=1):
        # Renvoie les n premières lettres
        return self.data[:n]

    def tail(self, n=1):
        # Renvoie les n dernières lettres
        return self.data[-n:]
    
    # ajout de méthode
    def len(self, n=1):
        
        return self.len(UserString)

s1 = MyString("prepabigdata")
print(s1.data)       # affiche: prepabigdata
print(s1.head())     # affiche: p
print(s1.head(2))    # affiche: pr
print(s1.tail())     # affiche: a
print(s1.tail(3))    # affiche: ata


# In[ ]:




