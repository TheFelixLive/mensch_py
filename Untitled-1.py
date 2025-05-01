import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Testing")

clock = pygame.time.Clock()

# Window icon
icon = pygame.image.load('ui/icon.png') 
pygame.display.set_icon(icon)

test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My game", False, "black")

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    # Inputs
    for event in pygame.event.get():
        # Quitting
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    

    screen.blit(snail_surface,snail_rect)
    if snail_rect.right > 0:
        snail_rect.x -= 1
    else:
        snail_rect.right = 800

    player_rect.left += 1
    screen.blit(player_surface,player_rect)

    pygame.display.update()
    clock.tick(60)

# https://youtu.be/AY9MnQ4x3zk?t=3832