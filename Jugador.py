class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.premio = 0
        self.categoria = 1

    def getNombre(self):
        return self.nombre

    def setPremio(self, premio):
        self.premio = premio

    def getPremio(self):
        return self.premio

    def acumularPremio(self, premio):
        self.premio += premio