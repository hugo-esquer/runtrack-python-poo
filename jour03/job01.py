class Ville:
    def __init__(self, nom, nombre):
        self.__nom = nom
        self.__nombre = nombre

    def ajout_nombre(self):
        self.__nombre += 1
    
    def get_nombre(self):
        return self.__nombre

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajout_nombre()

paris = Ville("Paris", 1000000)
print(f"Population de la ville de Paris: {paris.get_nombre()} habitants")

marseille = Ville("Marseille", 861635)
print(f"Population de la ville de Marseille: {marseille.get_nombre()} habitants")

jhon = Personne("Jhon", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Mise a jour de la population de la ville de Paris {paris.get_nombre()} habitants")
print(f"Mise a jour de la population de la ville de Marseille {marseille.get_nombre()} habitants")