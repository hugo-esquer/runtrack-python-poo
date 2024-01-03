class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

        self.__disponible = True

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
        if type(pages) == int :
            self.__pages = pages
        else:
            print("mauvais type")

    def verification(self):
        if self.__disponible:
            return True
        else:
            return False
    
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
        else:
            print("Le livre est disponible")

LSDA = Livre("Le Retour du Roi", "J.R.R. Tolkien", 722)
print(LSDA.get_titre())
print(LSDA.get_auteur())
print(LSDA.get_pages())

LSDA.set_titre("Un Nouvel Espoir")
LSDA.set_auteur("George Lucas")
LSDA.set_pages(500)
print(LSDA.get_titre())
print(LSDA.get_auteur())
print(LSDA.get_pages())

print(LSDA.verification())
LSDA.emprunter()
LSDA.emprunter()
LSDA.rendre()
LSDA.rendre()