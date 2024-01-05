class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        if type(age) == int:
            self.age = age
    
class Eleve(Personne):
    def allerEnCours(self):
        print("je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        Personne.__init__(self, age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

cassius = Eleve()
cassius.bonjour()
cassius.allerEnCours()
cassius.modifierAge(15)
cassius.afficherAge()

paul = Professeur(40, "Français")
paul.bonjour()
paul.enseigner()