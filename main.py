import pygame
from ui.colors import white, black, green, red
from game.snake import Snake
from game.fruit import Fruit
from game.score import Score
from game.sound_manager import SoundManager
from ui.intro_screen import intro_screen
from ui.game_over_screen import game_over_screen

pygame.init()
pygame.mixer.init()

window_x = 720
window_y = 480
FONT_NAME = 'times new roman'
MAIN_FONT = pygame.font.SysFont(FONT_NAME, 50)
BUTTON_FONT = pygame.font.SysFont(FONT_NAME, 30)
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')
fps = pygame.time.Clock()

snake_texture = pygame.image.load('assets/snake_texture.png')
snake_texture = pygame.transform.scale(snake_texture, (10, 10))
apple = pygame.image.load('assets/apple.png')
apple = pygame.transform.scale(apple, (10, 10))

def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != 'DOWN':
                snake.change_direction('UP')
            if event.key == pygame.K_s and snake.direction != 'UP':
                snake.change_direction('DOWN')
            if event.key == pygame.K_a and snake.direction != 'RIGHT':
                snake.change_direction('LEFT')
            if event.key == pygame.K_d and snake.direction != 'LEFT':
                snake.change_direction('RIGHT')

def update_game(snake, fruit, score, sound_manager):
    snake.move()

    if snake.check_fruit_collision(fruit.position):
        score.increment(10)
        snake.grow()
        fruit.spawn()
        sound_manager.play_eat_sound()

def render_game(snake, fruit, score, game_window):
    game_window.fill(black)
    for pos in snake.body:
        game_window.blit(snake_texture, pygame.Rect(pos[0], pos[1], 10, 10))
    game_window.blit(apple, pygame.Rect(fruit.position[0], fruit.position[1], 10, 10))
    score.show(game_window, white, FONT_NAME, 20)

def check_game_over(snake, window_x, window_y, sound_manager, score):
    if snake.check_boundary_collision(window_x, window_y) or snake.check_self_collision():
        sound_manager.play_game_over_sound()
        final_score = score.get_score()
        return final_score
    return None

def game_loop():
    snake = Snake()
    fruit = Fruit(window_x, window_y)
    score = Score()
    sound_manager = SoundManager()

    running = True

    while running:
        handle_events(snake)
        update_game(snake, fruit, score, sound_manager)

        final_score = check_game_over(snake, window_x, window_y, sound_manager, score)
        if final_score is not None:
            result = game_over_screen(game_window, window_x, window_y, MAIN_FONT, BUTTON_FONT, final_score)
            pygame.display.update()
            if result == "restart":
                return
            else:
                running = False

        render_game(snake, fruit, score, game_window)

        pygame.display.update()
        fps.tick(snake.speed)

if intro_screen(game_window, window_x, window_y, MAIN_FONT, BUTTON_FONT) == "start":
    while True:
        game_loop()

pygame.quit()
