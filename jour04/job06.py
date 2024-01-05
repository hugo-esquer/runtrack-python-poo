class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de portes = {self.portes}")

    def demarrer(self):
        print("Vroum, vroum je suis Flash McQueen")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = 2

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Nombre de roue = {self.roue}")

    def demarrer(self):
        print("Je n'ai besoin de personne en Harley Davidson")

classeA = Voiture("Mercedes", "Classe A", 2020, 18500)
classeA.informationVehicule()
print("")
vmax = Moto("Yamaha", "1200 Vmax", 1987, 4500)
vmax.informationVehicule()
print("")
classeA.demarrer()
vmax.demarrer()