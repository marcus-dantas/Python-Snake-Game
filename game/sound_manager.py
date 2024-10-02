import pygame

class SoundManager:
    def __init__(self):
        self.eat_sound = pygame.mixer.Sound('assets/eat.wav')
        self.game_over_sound = pygame.mixer.Sound('assets/game_over.wav')

    def play_eat_sound(self):
        pygame.mixer.Sound.play(self.eat_sound)

    def play_game_over_sound(self):
        pygame.mixer.Sound.play(self.game_over_sound)
