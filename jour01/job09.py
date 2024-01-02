class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return (self.prixHT * self.TVA / 100) + self.prixHT
    
    def afficher(self):
        return [self.nom, self.prixHT, self.TVA, self.CalculerPrixTTC()]
    
    def changerNom(self, n):
        self.nom = n

    def changerPrix(self, p):
        self.prixHT = p

    def afficherNom(self):
        return self.nom
    
    def afficherPrix(self):
        return self.prixHT
    
    def afficherTVA(self):
        return self.TVA
    
biere = Produit("biere", 3.5, 20)
jean = Produit("Jean", 100, 20)
whisky = Produit("whisky", 34.5, 20)

print(f"Le prix de la {biere.nom} est de {biere.CalculerPrixTTC()}")
print(f"Le prix d'un {jean.nom} est de {jean.CalculerPrixTTC()}")
print(f"Le prix du {whisky.nom} est de {whisky.CalculerPrixTTC()}")

biere.changerNom("IPA")
biere.changerPrix(8)
print(f"Le nouveau prix de la {biere.nom} est de {biere.CalculerPrixTTC()}")

jean.changerNom("Levis")
jean.changerPrix(130)
print(f"Le nouveau prix de la {jean.nom} est de {jean.CalculerPrixTTC()}")

whisky.changerNom("Chivas")
whisky.changerPrix(34)
print(f"le nouveau prix du {whisky.nom} est de {whisky.CalculerPrixTTC()}")

print(biere.afficher())
print(biere.afficherNom())
print(biere.afficherPrix())
print(biere.afficherTVA())