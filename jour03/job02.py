class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numero de compte: {self.__numero}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde}")

    def afficherSolde(self):
        print(f"Solde du compte {self.__numero}: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"Le nouveau solde du compte {self.__numero} est: {self.__solde}")

    def retrait(self, montant):
        if type(montant) == int and self.__solde > montant:
            self.__solde -= montant
            print(f"Le nouveau solde du compte {self.__numero} est: {self.__solde}")
            return True
        elif type(montant) == int and self.__decouvert:
            self.__solde -= montant
            print(f"Le nouveau solde du compte {self.__numero} est: {self.__solde}")
            return True
        else:
            print("Le solde n'est pas suffisant pour le retrait")
            return False
    
    def agios(self, jours, taux):
        if self.__solde < 0:
            self.__solde += self.__solde * jours * (taux/100) /365
            print(f"Le nouveau solde du compte {self.__numero} est: {self.__solde}")

    def virement(self, ref, compte, montant):
        if ref.retrait(montant):
            print("Le virement a été effectué")
            compte.versement(montant)
        else:
            print("Vous n'avez pas les fonds pour ce virement")

compte = CompteBancaire(132, "Bezos", "Jeff", 1000000, False)
compte.afficher()
compte.afficherSolde()
compte.versement(100)
compte.retrait(100)
compte.retrait(1000001)

compte2 = CompteBancaire(678, "Musk", "Elon", -600, True)
compte2.afficher()
compte2.agios(10, 18)
compte.virement(compte, compte2, 1000)
compte.virement(compte, compte2, 1000000)
compte2.retrait(998)