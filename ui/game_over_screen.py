import pygame
from ui.colors import white, black, green, red
from ui.buttons import draw_button

def game_over_screen(game_window, window_x, window_y, main_font, button_font, score):
    game_over_text = main_font.render(f"Your Final Score is : {score}", True, white)
    game_over_rect = game_over_text.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(game_over_text, game_over_rect)

    play_again_button = draw_button(game_window, 'Play Again', (window_x/2 - 75, window_y/2, 150, 50), green, button_font, black)
    quit_button = draw_button(game_window, 'Quit', (window_x/2 - 75, window_y/2 + 100, 150, 50), red, button_font, black)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    return "restart"
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()
