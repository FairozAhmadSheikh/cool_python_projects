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
