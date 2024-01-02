matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class Personnage:
    x = 0
    y = 0
    pos = matrice[y][x]

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1
    
    def bas(self):
        self.y +=1
    
    def haut(self):
        self.y -= 1
    
    def position(self):
        return (self.x, self.y)
    
joueur = Personnage()
print(joueur.position())
joueur.bas()
joueur.droite()
print(joueur.position())