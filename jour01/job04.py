class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"{self.nom} {self.prenom}"

Hugo = Personne("Hugo", "ESQUER")
Tom = Personne("Tom", "CLAVIS")
Val = Personne("Valentin", "BEAUSAERT")

print(f"Je suis {Hugo.SePresenter()}")
print(f"Je suis {Tom.SePresenter()}")
print(f"Je suis {Val.SePresenter()}")