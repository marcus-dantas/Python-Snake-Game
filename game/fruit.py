import random

class Fruit:
    def __init__(self, window_x, window_y, block_size=10):
        self.window_x = window_x
        self.window_y = window_y
        self.block_size = block_size
        self.spawn()

    def spawn(self):
        self.position = [random.randrange(1, self.window_x // self.block_size) * self.block_size,
                         random.randrange(1, self.window_y // self.block_size) * self.block_size]
