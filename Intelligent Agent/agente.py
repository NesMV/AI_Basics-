class Agente:
    def __init__(self, mundo, vidas=5):
        self.mundo = mundo
        self.posicion = mundo.start
        self.vidas = vidas

    def mover_a(self, posicion):
        if self.mundo.grid[posicion[1]][posicion[0]] == 3:  # Peligro
            self.vidas -= 1
        elif self.mundo.grid[posicion[1]][posicion[0]] == 2:  # Item
            self.mundo.grid[posicion[1]][posicion[0]] = 0  # Recoger el item

        self.posicion = posicion

    def esta_vivo(self):
        return self.vidas > 0
