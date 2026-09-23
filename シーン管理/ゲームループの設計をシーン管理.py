import sys
import pygame # pyright: ignore[reportMissingImports]

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 100, 255)

pygame.init()
screen = pygame.display.set_index = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)
)
pygame.display.set_caption("ゲームループとシーン管理")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

current_scene = "TITLE"
is_game_running = True

player_x = 300 
player_y = 200
player_speed = 5

def update_title(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "GAME"
    return "TITLE"
        
def draw_title():
    screen.fill(COLOR_BLACK)
    title_text = font.render("TITLE SCREEN", True, COLOR_WHITE)
    sub_text = font.render("PRESS ENTER to Start", True, COLOR_WHITE)
    screen.blit(title_text, (200, 150))
    screen.blit(sub_text, (150, 250))

def update_game(events):
    global player_x, player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "TITLE"
    
    return "GAME"

def draw_game():
    screen.fill(COLOR_BLACK)
    pygame.draw.rect(screen, COLOR_BLUE, (player_x, player_y, 40, 40))

    info_text = font.render("ESC to Title", True, COLOR_WHITE)
    screen.blit(info_text, (10,10))

while is_game_running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_game_running = False
    
    if current_scene == "TITLE":
        current_scene = update_title(events)
        draw_title()

    elif current_scene == "GAME":
        current_scene =update_game(events)
        draw_game()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

