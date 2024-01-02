class Operation:
    def __init__(self, nombre1=5, nombre2=8):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

test = Operation()
print(test.addition())