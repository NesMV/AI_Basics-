import pygame
import tkinter as tk
from tkinter import messagebox
from mundo import Mundo
from agente import Agente
from algoritmo import a_estrella
import time

# Inicializar el entorno de Pygame
pygame.init()

# Dimensiones del mundo
width, height = 10, 10
num_obstacles = 20
num_items = 2  # Reducción del número de items a 2

# Crear el mundo y el agente
mundo = Mundo(width, height, num_obstacles, num_items)
agente = Agente(mundo, vidas=5)  # Aumento del número de vidas a 5

# Configuración de la ventana
size = (width * 40, height * 40 + 100)  # Espacio adicional para la leyenda y contador de vidas
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Agente Inteligente")

# Cargar íconos
icon_agente = pygame.image.load('icons/agent.png')
icon_obstaculo = pygame.image.load('icons/obstacle.png')
icon_item = pygame.image.load('icons/item.png')
icon_peligro = pygame.image.load('icons/danger.png')
icon_camino = pygame.image.load('icons/path.png')
icon_objetivo = pygame.image.load('icons/goal.png')

# Redimensionar íconos
icon_agente = pygame.transform.scale(icon_agente, (40, 40))
icon_obstaculo = pygame.transform.scale(icon_obstaculo, (40, 40))
icon_item = pygame.transform.scale(icon_item, (40, 40))
icon_peligro = pygame.transform.scale(icon_peligro, (40, 40))
icon_camino = pygame.transform.scale(icon_camino, (40, 40))
icon_objetivo = pygame.transform.scale(icon_objetivo, (40, 40))

# Colores
COLORS = {
    0: (255, 255, 255),   # Camino
    -1: (0, 0, 0),        # Obstáculo
    2: (0, 255, 0),       # Item
    3: (255, 0, 0),       # Peligro
}

# Fuente para el contador de vidas y la leyenda
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Función para dibujar el mundo
def draw_world():
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * 40, y * 40, 40, 40)
            color = COLORS.get(mundo.grid[y][x], (255, 255, 255))
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)  # Cambiar el color de la cuadrícula a gris claro
            if mundo.grid[y][x] == -1:
                screen.blit(icon_obstaculo, (x * 40, y * 40))
            elif mundo.grid[y][x] == 2:
                screen.blit(icon_item, (x * 40, y * 40))
            elif mundo.grid[y][x] == 3:
                screen.blit(icon_peligro, (x * 40, y * 40))
            elif (x, y) == mundo.goal:
                screen.blit(icon_objetivo, (x * 40, y * 40))
            else:
                screen.blit(icon_camino, (x * 40, y * 40))

    # Dibujar al agente
    screen.blit(icon_agente, (agente.posicion[0] * 40, agente.posicion[1] * 40))

# Función para dibujar el contador de vidas
def draw_lives():
    text = font.render(f'Vidas: {agente.vidas}', True, (0, 0, 0))
    screen.blit(text, (10, height * 40 + 10))

# Función para dibujar la leyenda
def draw_legend():
    legend_items = [
        ("Agente", icon_agente),
        ("Obstáculo", icon_obstaculo),
        ("Item", icon_item),
        ("Peligro", icon_peligro),
        ("Camino", icon_camino),
        ("Objetivo", icon_objetivo)
    ]
    for i, (label, icon) in enumerate(legend_items):
        y_offset = height * 40 + 40 + i * 30
        if icon:
            screen.blit(icon, (10, y_offset))
            text = small_font.render(label, True, (0, 0, 0))
            screen.blit(text, (50, y_offset + 10))

# Mostrar una ventana emergente si no se encuentra un camino
def show_no_path_message():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    messagebox.showinfo("Camino no encontrado", "No se encontró un camino posible. ¿Quieres volver a intentarlo?")
    root.destroy()

# Calcular el camino
camino = a_estrella(mundo, mundo.start, mundo.goal, mundo.items)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino")
    show_no_path_message()

# Bucle principal
running = True
camino_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Limpiar pantalla
    screen.fill((255, 255, 255))

    # Dibujar el mundo
    draw_world()

    # Dibujar el contador de vidas
    draw_lives()

    # Dibujar la leyenda
    draw_legend()

    # Mover al agente paso a paso
    if camino and agente.esta_vivo():
        if camino_index < len(camino):
            nueva_posicion = camino[camino_index]
            agente.mover_a(nueva_posicion)
            camino_index += 1
        else:
            print("Agente ha llegado al objetivo o no hay más pasos en el camino")

    # Actualizar la pantalla
    pygame.display.flip()

    # Pausar brevemente para ver el movimiento
    time.sleep(0.5)

pygame.quit()
