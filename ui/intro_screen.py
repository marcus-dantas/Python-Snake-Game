import pygame
from ui.colors import white, black, green, red
from ui.buttons import draw_button

def intro_screen(game_window, window_x, window_y, main_font, button_font):
    intro_text = main_font.render('Welcome to Snake Game', True, white)
    intro_rect = intro_text.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(intro_text, intro_rect)

    start_button = draw_button(game_window, 'Start Game', (window_x/2 - 75, window_y/2, 150, 50), green, button_font, black)
    quit_button = draw_button(game_window, 'Quit', (window_x/2 - 75, window_y/2 + 100, 150, 50), red, button_font, black)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()
