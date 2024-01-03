class Commande:
    def __init__(self, numero, statut):
        self.__numero = numero
        self.__liste = {}
        self.__statut = statut

    def ajout(self, plat, prix):
        self.__liste[plat] = prix

    def annuler(self):
        self.__statut = "annulée"

    def __total(self):
        total = 0
        prix = list(self.__liste.values())
        for i in range(len(self.__liste)):
            total += prix[i]
        total += self.tva()
        return total
    
    def tva(self):
        TVA = 20
        total_TVA = 0
        prix = list(self.__liste.values())
        for i in range(len(self.__liste)):
            total_TVA += (prix[i] * TVA/100)
        return total_TVA
        
    def afficher(self):
       print(self.__liste)
       print(self.__total())
       print(self.__statut)


commande1 = Commande(1, "en cours")
commande1.ajout("pizza", 12)
commande1.ajout("pates", 10)
commande1.ajout("soupe", 8)

commande1.annuler()
commande1.afficher()