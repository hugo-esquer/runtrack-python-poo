class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur
    
rectangle = Rectangle(17, 9)
rectangle.set_longueur(19)
rectangle.set_largeur(10)
print(f"la longueur du rectangle est de: {rectangle.get_longueur()}")
print(f"la largueur du rectangle est de: {rectangle.get_largeur()}")
print(f"le perimètre du rectangle est de: {rectangle.perimetre()}")
print(f"la surface du rectangle est de: {rectangle.surface()}")

parallelepipede = Parallelepipede(26, 18, 7)
parallelepipede.set_longueur(24)
parallelepipede.set_largeur(20)
print(f"la longueur du parallelepipède est de: {parallelepipede.get_longueur()}")
print(f"la largeur du parallelepipède est de: {parallelepipede.get_largeur()}")
print(f"le volume du parallelepipède est de: {parallelepipede.volume()}")
