# ui.py

import tkinter as tk
from fuzzy_logic import FuzzyLogicController

class FuzzyUI:
    def __init__(self, root):
        self.controller = FuzzyLogicController()
        self.root = root
        self.root.title("Control de Temperatura - Lógica Difusa")

        self.temp_actual_label = tk.Label(root, text="Temperatura Actual (°C)")
        self.temp_actual_label.pack()
        self.temp_actual_slider = tk.Scale(root, from_=0, to=30, orient=tk.HORIZONTAL)
        self.temp_actual_slider.pack()

        self.temp_desired_label = tk.Label(root, text="Temperatura Deseada (°C)")
        self.temp_desired_label.pack()
        self.temp_desired_slider = tk.Scale(root, from_=15, to=30, orient=tk.HORIZONTAL)
        self.temp_desired_slider.pack()

        self.result_button = tk.Button(root, text="Calcular", command=self.calculate)
        self.result_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        temp_actual = self.temp_actual_slider.get()
        temp_desired = self.temp_desired_slider.get()
        comp_output, fan_output = self.controller.infer(temp_actual, temp_desired)
        result_text = f"Potencia del Compresor: {comp_output:.2f}%\nVelocidad del Ventilador: {fan_output:.2f}%"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FuzzyUI(root)
    root.mainloop()
