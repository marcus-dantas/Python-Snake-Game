import pygame

def draw_button(game_window, text, position, color, font, text_color):
    button_rect = pygame.Rect(position)
    pygame.draw.rect(game_window, color, button_rect)
    button_text = font.render(text, True, text_color)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    game_window.blit(button_text, button_text_rect)
    return button_rect
