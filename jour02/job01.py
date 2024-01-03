class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, i):
        if type(i)==int or type(i)==float:
            self.__longueur = i
        else:
            print("mauvais type")
    
    def set_largeur(self, i):
        if type(i)==int or type(i)==float:
            self.__largeur = i
        else:
            print("mauvais type")

rectangle = Rectangle(10, 5)
print(rectangle.get_longueur())
print(rectangle.get_largeur())
rectangle.set_longueur(27)
rectangle.set_largeur(18)
print(rectangle.get_longueur())
print(rectangle.get_largeur())