import random

class Mundo:
    def __init__(self, width, height, num_obstacles, num_items):
        self.width = width
        self.height = height
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.items = []
        self.generar_obstaculos(num_obstacles)
        self.generar_items(num_items)

    def generar_obstaculos(self, num_obstacles):
        count = 0
        while count < num_obstacles:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) != self.start and (x, y) != self.goal and self.grid[y][x] == 0:
                self.grid[y][x] = -1
                count += 1

    def generar_items(self, num_items):
        count = 0
        while count < num_items:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) != self.start and (x, y) != self.goal and self.grid[y][x] == 0:
                self.grid[y][x] = 2
                self.items.append((x, y))
                count += 1

    def obtener_vecinos(self, posicion):
        x, y = posicion
        vecinos = []
        if x > 0 and self.grid[y][x-1] != -1:
            vecinos.append((x-1, y))
        if x < self.width - 1 and self.grid[y][x+1] != -1:
            vecinos.append((x+1, y))
        if y > 0 and self.grid[y-1][x] != -1:
            vecinos.append((x, y-1))
        if y < self.height - 1 and self.grid[y+1][x] != -1:
            vecinos.append((x, y+1))
        return vecinos
