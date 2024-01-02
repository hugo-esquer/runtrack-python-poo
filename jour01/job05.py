class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(self.x, self.y)

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, j):
        self.x = j
    
    def changerY(self, j):
        self.y = j

point = Point(6, 8)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(10)
point.afficherLesPoints()
point.changerY(42)
point.afficherLesPoints()