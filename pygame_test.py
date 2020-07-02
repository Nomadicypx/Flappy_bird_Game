# -*-coding: utf-8-*-
import sys
import pygame
import random
import time


def random_speed():
    return random.randint(-50, 50), random.randint(-50, 50)


pygame.init()
size = width, height = 720, 640
color = (255, 255, 255)
screen = pygame.display.set_mode(size)
screen.fill(color)
background = pygame.image.load('background.jpg')
background = pygame.transform.smoothscale(background, size)
bird = pygame.image.load('bird_normal.png')
bird = pygame.transform.flip(bird, True, False)
bird = pygame.transform.smoothscale(bird, (width // 10, height // 6))
restart = pygame.image.load('restart.png')
birdrect = bird.get_rect()
speed_list_length = 4
speed = []
for i in range(0, speed_list_length):
    speed.append(list(random_speed()))

clock = pygame.time.Clock()
pipe = pygame.image.load('pipe.png')
print(pipe.get_rect())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    step = speed[random.randint(0, speed_list_length - 1)]
    birdrect = birdrect.move(step)
    if birdrect.left < 0 or birdrect.right > width:
        step[0] = 0 - step[0]
    if birdrect.top < 0 or birdrect.bottom < height:
        step[1] = 0 - step[1]
    screen.blit(background, (0, 0))
    screen.blit(bird, birdrect)
    screen.blit(pipe, (size[0] - 50, 0))
    screen.blit(restart, (20, 10))
    pygame.display.flip()
    clock.tick(5)
pygame.quit()
