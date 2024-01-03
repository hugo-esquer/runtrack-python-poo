class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_pages(self):
        return self.__pages
    
    def set_titre(self, titre):
        self.__titre = titre
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_pages(self, pages):
        if type(pages) == int and pages >= 0 :
            self.__pages = pages
        else:
            print("mauvais type")
    
LSDA = Livre("La Fraternité de l'Anneau", "J.R.R Tolkien", 722)
print(LSDA.get_auteur())
print(LSDA.get_titre())
print(LSDA.get_pages())
LSDA.set_auteur("John Ronald Reuel Tolkien")
LSDA.set_titre("Les Deux Tours")
LSDA.set_pages(597)
print(LSDA.get_auteur())
print(LSDA.get_titre())
print(LSDA.get_pages())
LSDA.set_pages(-34)