import pygame

class Score:
    def __init__(self):
        self.score = 0

    def increment(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def get_score(self):
        return self.score

    def show(self, game_window, color, font_name, size, x=0, y=0):
        score_font = pygame.font.SysFont(font_name, size)
        score_surface = score_font.render(f"Score : {self.score}", True, color)
        score_rect = score_surface.get_rect(topleft=(x, y))
        game_window.blit(score_surface, score_rect)
