class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.speed = 15
        self.grow_snake = False

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'


    def move(self):
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10

        self.body.insert(0, list(self.position))

        if not self.grow_snake:
            self.body.pop()
        else:
            self.grow_snake = False

    def grow(self):
        self.grow_snake = True
        self.speed += 1

    def check_fruit_collision(self, fruit_position):
        if self.position == fruit_position:
            return True
        return False
    
    def check_boundary_collision(self, window_x, window_y):
        if self.position[0] < 0 or self.position[0] >= window_x or self.position[1] < 0 or self.position[1] >= window_y:
            return True
        return False

    def check_self_collision(self):
        for block in self.body[1:]:
            if self.position == block:
                return True
        return False
