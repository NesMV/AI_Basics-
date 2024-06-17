# Modelo ART

# art.py
import numpy as np

class ART1:
    def __init__(self, input_size, vigilance=0.75):
        self.input_size = input_size
        self.vigilance = vigilance
        self.weights = []
        self.categories = {}

    def reset(self):
        self.weights = []
        self.categories = {}

    def train(self, input_pattern):
        if len(self.weights) == 0:
            self.weights.append(input_pattern)
            return 0

        for i, w in enumerate(self.weights):
            if self.match(input_pattern, w):
                self.weights[i] = self.update_weights(w, input_pattern)
                return i

        self.weights.append(input_pattern)
        return len(self.weights) - 1

    def match(self, input_pattern, weight):
        similarity = np.sum(np.minimum(input_pattern, weight)) / np.sum(input_pattern)
        return similarity >= self.vigilance

    def update_weights(self, weight, input_pattern):
        return np.minimum(weight, input_pattern)
