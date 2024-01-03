class Student:
    def __init__(self, nom, prenom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def add_credits(self, add):
        if add > 0:
            self.__credits = self.__credits + add

    def get_credits(self):
        return self.__credits
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"
    
    def studentInfo(self):
        self.__level = self.__studentEval()
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero}")
        print(f"Niveau = {self.__level}")
        
    

etudiant = Student("John", "Doe", 145)
etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(10)
print(f"Le nombre de credits de John Doe est de {etudiant.get_credits()} points")
etudiant.add_credits(45)

print(etudiant.get_credits())
etudiant.studentInfo()