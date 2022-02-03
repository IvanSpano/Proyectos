class Persona:
    def __init__(self,Nombre,Edad):
        self.Edad = Edad   
        self.Nombre = Nombre

    def cumpleaños(self):
        self.Edad = self.Edad + 1


p = Persona("Juan", 21)
p.cumpleaños()
print(f"{p.Nombre} cumple {p.Edad} años")