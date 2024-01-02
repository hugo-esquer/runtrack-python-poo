class Animal:
    age = 0
    prenom = ""

    def viellir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

chien = Animal()
print(f"L'age de l'animal {chien.age} ans")
chien.viellir()
print(f"L'age de l'animal {chien.age} ans")
chien.nommer("Vlad")
print(f"L'animal se nomme {chien.prenom}")