import tkinter as tk

class Visualizer:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        
        self.generation_label = tk.Label(self.root, text="Generation: 0")
        self.generation_label.pack()

        self.mutation_slider = tk.Scale(self.root, from_=0.01, to=0.5, resolution=0.01, orient=tk.HORIZONTAL, label="Mutation Rate")
        self.mutation_slider.set(self.algorithm.mutation_rate)
        self.mutation_slider.pack()

        self.tournament_slider = tk.Scale(self.root, from_=2, to=10, resolution=1, orient=tk.HORIZONTAL, label="Tournament Size")
        self.tournament_slider.set(self.algorithm.tournament_size)
        self.tournament_slider.pack()

        self.diversity_slider = tk.Scale(self.root, from_=0.01, to=0.5, resolution=0.01, orient=tk.HORIZONTAL, label="Diversity Threshold")
        self.diversity_slider.set(self.algorithm.diversity_threshold)
        self.diversity_slider.pack()

        self.similarity_slider = tk.Scale(self.root, from_=0.8, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, label="Similarity Threshold")
        self.similarity_slider.set(self.algorithm.similarity_threshold)
        self.similarity_slider.pack()

        self.root.update()

    def update(self, population, generation):
        self.canvas.delete("all")
        num_worlds = len(population)
        cols = int(num_worlds**0.5)
        size = population[0].size
        cell_width = 500 // size[1]
        cell_height = 500 // size[0]
        world_width = size[1] * cell_width
        world_height = size[0] * cell_height

        for idx, world in enumerate(population):
            x_offset = (idx % cols) * world_width
            y_offset = (idx // cols) * world_height
            self.draw_world(world, x_offset, y_offset)

        self.generation_label.config(text=f"Generation: {generation}")

        # Update algorithm parameters from sliders
        self.algorithm.mutation_rate = self.mutation_slider.get()
        self.algorithm.tournament_size = self.tournament_slider.get()
        self.algorithm.diversity_threshold = self.diversity_slider.get()
        self.algorithm.similarity_threshold = self.similarity_slider.get()

        self.root.update()

    def draw_world(self, world, x_offset, y_offset):
        size = world.size
        cell_width = 500 // size[1]
        cell_height = 500 // size[0]

        for i in range(size[0]):
            for j in range(size[1]):
                x0 = x_offset + j * cell_width
                y0 = y_offset + i * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
                color = self.get_color(world.grid[i][j])
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def get_color(self, value):
        colors = ["#0000FF", "#00FF00", "#FF0000", "#FFFF00", "#FF00FF", "#00FFFF"]
        return colors[value % len(colors)]

    def show_final(self):
        self.root.mainloop()
