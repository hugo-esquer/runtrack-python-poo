class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele
    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee
    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
        else:
            print("pas assez d'essence")
    def arreter(self):
        self.__en_marche = False

voiture = Voiture("Ford", "Mustang", 1969, 18000)

print(f"Mon ancienne voiture est une {voiture.get_marque()} {voiture.get_modele()} de {voiture.get_annee()} avec {voiture.get_kilometrage()} kilomètre")

voiture.set_marque("Renault")
voiture.set_modele("Twingo")
voiture.set_annee(2023)
voiture.set_kilometrage(0)

print(f"Ma nouvelle voiture est une {voiture.get_marque()} {voiture.get_modele()} de {voiture.get_annee()} avec {voiture.get_kilometrage()} kilomètre")

voiture.demarrer()
voiture.arreter()