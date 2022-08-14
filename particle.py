import random

class Particle():

    def __init__(self, line_length: int, position: int):
        self.position = position
        self.direction = random.choices([-1, 1])[0]

    def __str__(self):
        return (f"pos: {self.position} \n dir: {self.direction_text}")

    @property
    def direction_text(self):
        return "going left" if self.direction == -1 else "going right"

    def move(self):
        self.position = self.position + self.direction


    def reverse_direction(self):
        self.direction = self.direction * -1











