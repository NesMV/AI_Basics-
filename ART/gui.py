# GUI

import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import messagebox
import numpy as np
from art import ART1

class PatternApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconocimiento de patrones con ART")
        self.canvas_size = 300
        self.cell_size = 40
        self.pattern_size = self.canvas_size // self.cell_size

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-3>", self.erase)
        self.canvas.bind("<B3-Motion>", self.erase)

        self.pattern = np.zeros((self.pattern_size, self.pattern_size))
        self.art = ART1(self.pattern_size * self.pattern_size)

        self.recognize_button = tk.Button(root, text="Reconocer patrón", command=self.recognize_pattern)
        self.recognize_button.pack()

        self.clear_button = tk.Button(root, text="Limpiar Grid", command=self.clear_canvas)
        self.clear_button.pack()

        self.category_label = tk.Label(root, text="Categoría: None")
        self.category_label.pack()

        self.draw_grid()

        self.menu = tk.Menu(root)
        self.menu.add_command(label="Ayuda", command=self.show_help)
        root.config(menu=self.menu)

    def draw_grid(self):
        for i in range(self.pattern_size):
            for j in range(self.pattern_size):
                x0 = i * self.cell_size
                y0 = j * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="gray")

    def draw(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.pattern_size and 0 <= y < self.pattern_size:
            self.pattern[y, x] = 1
            x0 = x * self.cell_size
            y0 = y * self.cell_size
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="gray")

    def erase(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if 0 <= x < self.pattern_size and 0 <= y < self.pattern_size:
            self.pattern[y, x] = 0
            x0 = x * self.cell_size
            y0 = y * self.cell_size
            x1 = x0 + self.cell_size
            y1 = y0 + self.cell_size
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="gray")

    def recognize_pattern(self):
        flat_pattern = self.pattern.flatten()
        category, category_name = self.get_category(flat_pattern)
        if category is not None:
            self.category_label.config(text=f"Categoría: {category_name}")
            self.display_pattern(self.art.weights[category])

    def get_category(self, pattern):
        category = self.art.train(pattern)
        if category is not None:
            if category in self.art.categories:
                return category, self.art.categories[category]
            else:
                category_name = askstring("Nombre de categoría", "Ingresa un nombre para la categoría:")
                if category_name:
                    self.art.categories[category] = category_name
                    return category, category_name
        return None, "None"

    def display_pattern(self, pattern):
        self.canvas.delete("all")
        self.draw_grid()
        for i in range(self.pattern_size):
            for j in range(self.pattern_size):
                color = 'black' if pattern[i * self.pattern_size + j] == 1 else 'white'
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.pattern = np.zeros((self.pattern_size, self.pattern_size))
        self.draw_grid()
        self.category_label.config(text="Categoría: None")

    def show_help(self):
        help_text = """
        Reconocimiento de patrones con ART
        
        Este programa le permite dibujar patrones y reconocerlos utilizando el algoritmo ART (Teoría de Resonancia Adaptativa).
        
        Modo de uso:
        1. Dibuje un patrón en la cuadrícula haciendo clic o arrastrando con el botón izquierdo del mouse.
        2. Utilice el botón derecho del mouse para borrar partes del patrón.
        3. Haga clic en 'Reconocer patrón' para clasificar el patrón dibujado.
        4. Utilice 'Borrar' para restablecer la cuadrícula.
        
        """
        messagebox.showinfo("Help", help_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PatternApp(root)
    root.mainloop()
