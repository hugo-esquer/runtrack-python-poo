import random
class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        cible.vie -= random.randint(1, 10)
        print(f"la vie de {cible.nom} est de {cible.vie}")

    def statut(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = 0
        self.ryu = ""
        self.ken = ""

    def choisirNiveau(self):
        self.niveau = int(input("Entrer un entier positif pour le niveau: "))

    def lancerJeu(self):
        self.choisirNiveau()
        vie = self.niveau * 10
        self.ryu = Personnage("ryu", vie)
        self.ken = Personnage("ken", vie)

        while self.ryu.statut() and self.ken.statut() :
            self.ryu.attaquer(self.ken)
            if not self.ken.statut():
                break
            self.ken.attaquer(self.ryu)

        self.finDePartie()
        
    def finDePartie(self):
        if self.ryu.vie <= 0 and self.ken.vie > 0:
            print("Ken a gagné !")
        if self.ken.vie <= 0 and self.ryu.vie > 0:
            print("Ryu a gagné !")

streetFighter = Jeu()
streetFighter.lancerJeu()
