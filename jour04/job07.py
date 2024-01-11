import random

class carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def afficher(self):
        return f"{self.valeur} de {self.couleur}"

class jeu:
    def __init__(self):
        self.paquet = self.creerPaquet()

    def creerPaquet(self):
        couleurs = ["pique", "coeur", "carreau", "trefle"]
        valeurs = ["as", 2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi"]
        paquet = []
        for i in couleurs:
            for j in valeurs:
                paquet.append(carte(j, i))
        random.shuffle(paquet)
        return paquet

    def tirerUneCarte(self):
        return self.paquet.pop()

    def valeurCarte(self, carte):
        if carte.valeur in ["valet", "dame", "roi"]:
            return 10
        elif carte.valeur == "as":
            return 11
        else:
            return carte.valeur
        
    #valeur de la main
    def valeurMain(self, main):
        total = 0
        for carte in main:
            total += self.valeurCarte(carte)
        for carte in main:
            if carte.valeur == "as" and total > 21:
                total -= 10
        return total

    #set up mains des joueurs
    def mainJoueur(self):
        main = []
        for i in range(0, 2):
            main.append(self.tirerUneCarte())
        print(f"La main du joueur est: {main[0].afficher()}, {main[1].afficher()}")
        return main

    def mainCroupier(self):
        main = []
        for i in range(0, 2):
            main.append(self.tirerUneCarte())
        print(f"La main du Croupier est: {main[0].afficher()}")
        return main
    
    #tour du joueur
    def tourJoueur(self, main):
        jeu = input("Tirer une carte ? o/n ")
        tailleMain = 2
        while jeu.lower() == "o":
            carte = self.tirerUneCarte()
            main.append(carte)
            tailleMain +=1
            totalMain = ""
            for x in range(0, tailleMain):
                totalMain += f"{main[x].afficher()}, "
            print(f"votre main est: {totalMain}")
            if self.valeurMain(main) > 21:
                self.win(main, croupier)
                return "loose", main
            jeu = input("Tirer une autre carte ? o/n ")
        return None, main

    #tour du croupier
    def tourCroupier(self, main, joueur):
        tailleMain = 2
        totalMain = ""
        for x in range (0, tailleMain):
            totalMain += f"{main[x].afficher()}, "
        print(f"Le coupier a: {totalMain}")
        while self.valeurMain(main) < 17 and self.valeurMain(main) < self.valeurMain(joueur):
            carte = self.tirerUneCarte()
            main.append(carte)
            tailleMain += 1
            totalMain = ""
            for x in range(0, tailleMain):
                totalMain += f"{main[x].afficher()}, "
            print(f"La main du croupier est: {totalMain}")

    #resultat
    def win(self, joueur, croupier):
        if self.valeurMain(joueur) > 21:
            print("Désolé vous avez perdu")
        elif self.valeurMain(croupier) > 21 or self.valeurMain(joueur) > self.valeurMain(croupier):
            print("Bien joué, vous avez gagné !")
        else:
            print("La banque gagne")

blackJack = jeu()
joueur = blackJack.mainJoueur()
if blackJack.valeurMain(joueur) == 21:
    print("Winner winner chiken dinner !")
else:
    croupier = blackJack.mainCroupier()
    game, mainJoueur = blackJack.tourJoueur(joueur)
    if game != "loose":
        blackJack.tourCroupier(croupier, mainJoueur)
        blackJack.win(joueur, croupier)