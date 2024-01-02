from math import *

class Cercle:
    def __init__(self, rayon=4):
        self.rayon = rayon
    
    def changerRayon(self, n):
        self.rayon = n
    
    def circonférence(self):
        return 2*self.rayon*pi
    
    def aire(self):
        return pi*self.rayon**2
    
    def diametre(self):
        return self.rayon*2

    def afficherInfos(self):
        print(self.rayon)
        print(self.circonférence())
        print(self.aire())
        print(self.diametre())

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.afficherInfos()
print(f"La circonférence du cercle 1 est de {cercle1.circonférence()}")
print(f"Le diamètre du cercle 1 est de {cercle1.diametre()}")
print(f"L'aire du cercle 1 est de {cercle1.aire()}")

cercle2.afficherInfos()
print(f"Le circonférence du cercle 2 est de {cercle2.circonférence()}")
print(f"Le diamètre du cercle 2 est de {cercle2.diametre()}")
print(f"L'aire du cercle 2 est de {cercle2.aire()}")