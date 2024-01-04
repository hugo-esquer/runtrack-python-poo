class Joueur:
    def __init__(self, nom, prenom, position, buts, passesDe, jaunes, rouges):
        self.nom = nom
        self.prenom = prenom
        self.position = position
        self.buts = buts
        self.passesDe = passesDe
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passesDe +=1

    def recevoirUnCartonJaune(self):
        self.jaunes += 1

    def recevoirUnCartonRouge(self):
        self.rouges += 1

    def afficherStatistiques(self):
        print(f"{self.nom} a marqué {self.buts} buts et a {self.passesDe} passes décisives pour {self.jaunes} cartons jaunes et {self.rouges} cartons rouges")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        if joueur not in self.joueurs:
            self.joueurs.append(joueur)
        else:
            print("Le joueur est déjà dans l'équipe")

    def afficherStatistiquesJoueurs(self):
        for i in self.joueurs:
            i.afficherStatistiques()
        print("")

    def mettreAJourStatistiquesJoueur(self, nom, but, passesDe, jaunes, rouges):
       for joueur in self.joueurs:
           if joueur.nom == nom:
                joueur.buts = but
                joueur.passesDe = passesDe
                joueur.jaunes = jaunes
                joueur.rouges = rouges 

# création des joueurs
gardien = Joueur("Bolzinger", "Charles", "gardien", 0, 0, 0, 0)
demi_centre = Joueur("Mahé", "Kentin", "demi-centre", 7, 4, 0, 0)
arriere_gauche = Joueur("Briet", "Thibaud", "arriere gauche", 2, 6, 0, 1)
arriere_droit = Joueur("Men", "Dika", "arriere droit", 1, 7, 3, 0)
pivot = Joueur("Fabregas", "Ludovic", "pivot", 8, 9, 2, 1)
ailier_droit = Joueur("Lenne", "Yanis", "ailier droit", 6, 9, 6, 2)

#création des équipes
Bleus = Equipe("Les Bleus")
Bleus.ajouterJoueur(gardien)
Bleus.ajouterJoueur(demi_centre)
Bleus.ajouterJoueur(arriere_gauche)

Rouges = Equipe("Les Rouges")
Rouges.ajouterJoueur(arriere_droit)
Rouges.ajouterJoueur(pivot)
Rouges.ajouterJoueur(ailier_droit)

#afficher les stat des joueur par équipes
Bleus.afficherStatistiquesJoueurs()
Rouges.afficherStatistiquesJoueurs()

#mise a jour des stat du joueur
Rouges.mettreAJourStatistiquesJoueur("Fabregas", 0, 0, 0, 0)

#simuler un macth
demi_centre.marquerUnBut()
pivot.marquerUnBut()
ailier_droit.recevoirUnCartonJaune()
gardien.effectuerUnePasseDecisive()
arriere_gauche.marquerUnBut()
arriere_droit.recevoirUnCartonRouge()

#afficher les stat apres match
Bleus.afficherStatistiquesJoueurs()
Rouges.afficherStatistiquesJoueurs()