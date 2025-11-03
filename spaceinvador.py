import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_img = pygame.image.load('tank.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (60, 40))

bullet_img = pygame.Surface((7, 18), pygame.SRCALPHA)
pygame.draw.rect(bullet_img, (255, 255, 0), [0, 0, 7, 18])
bullet_speed = 9


enemy_imgs = [
    pygame.transform.scale(pygame.image.load('alien1.png').convert_alpha(), (48, 36)),
    pygame.transform.scale(pygame.image.load('alien2.png').convert_alpha(), (48, 36)),
    pygame.transform.scale(pygame.image.load('alien3.png').convert_alpha(), (48, 36))
]

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (70, 130, 180)  
        self.highlight_color = (100, 149, 237) 

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.highlight_color, self.rect)
            if click[0] == 1:  
                return True  
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        return False

def create_enemies():
    enemies = []
    for _ in range(8):
        image = random.choice(enemy_imgs)
        x = random.randint(0, SCREEN_WIDTH - 48)
        y = random.randint(60, 160)
        speed = random.choice([2, 3, 4])
        enemies.append({'img': image, 'x': x, 'y': y, 'speed': speed})
    return enemies

def reset_game():
    global player_x, player_y, bullets, enemies, score, lives, game_over
    player_x = (SCREEN_WIDTH - 60) // 2
    player_y = SCREEN_HEIGHT - 70
    bullets = []
    enemies = create_enemies()
    score = 0
    lives = 3
    game_over = False

def is_collision(x1, y1, x2, y2, threshold=32):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance < threshold