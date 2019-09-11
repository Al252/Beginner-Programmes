import pygame
import random
import os


print(os.getcwd())
pygame.init()

(width, height) = (500, 500)

win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Catch the Pope')



ch_x = 250
ch_y = 250
ch_width = 10
ch_height = 10
vel = 10
score = 0

food_x = random.randrange(0, width, vel)
food_y = random.randrange(0, height, vel)
food_width = 10
food_height = 10
food_colour = (250, 250, 250)
bg_colour = (150, 50, 150)
ch_colour = (0, 0, 0)

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif (ch_x + ch_width) > width or (ch_y + ch_height) > height or ch_x < 0 or ch_y < 0:
            print('Game Over')
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ch_x -= vel
    if keys[pygame.K_RIGHT]:
        ch_x += vel
    if keys[pygame.K_UP]:
        ch_y -= vel
    if keys[pygame.K_DOWN]:
        ch_y += vel
    win.fill(bg_colour)
    pygame.draw.rect(win, food_colour, (food_x, food_y, food_width, food_height))
    if (food_x == ch_x) and food_y == ch_y:
        eat = pygame.mixer.Sound("eating.wav")
        eat.play()
        food_x = random.randrange(0, 500, vel)
        food_y = random.randrange(0, 500, vel)
        pygame.draw.rect(win, food_colour, (food_x, food_y, food_width, food_height))
        score += 5
    pygame.draw.rect(win, ch_colour, (ch_x, ch_y, ch_width, ch_height))
    pygame.display.update()

print('Score: ', score)

pygame.quit()
