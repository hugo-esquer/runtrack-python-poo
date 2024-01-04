class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)
        else:
            print("La tache est deja dans la liste")
    
    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
        else:
            print("La tache n'est pas dans la liste")

    def marquerCommeFinie(self, tache):
        if tache in self.taches:
            tache.statut = "Terminer"
        else:
            print("La tache n'est pas dans la liste")

    def afficherListe(self):
        liste = []
        for i in self.taches:
            liste.append(i.titre)
        print(liste)

    def filterListe(self):
        liste = []
        for i in self.taches:
            if i.statut == "à faire":
                liste.append(i.titre)
        print(liste)

courses = Tache("courses", "faire les courses", "à faire")
coiffeur = Tache("coiffeur", "allez chez le coiffeur", "à faire")
menage = Tache("ménage", "faire le ménage", "à faire")
repas = Tache("repas", "préparer à manger", "à faire")
shopping = Tache("shopping", "faire du shopping", "à faire")

liste = ListeDeTaches()
liste.ajouterTache(courses)
liste.ajouterTache(coiffeur)
liste.ajouterTache(menage)
liste.ajouterTache(repas)
liste.ajouterTache(shopping)

liste.afficherListe()
liste.supprimerTache(repas)
liste.marquerCommeFinie(shopping)
liste.afficherListe()
liste.filterListe()