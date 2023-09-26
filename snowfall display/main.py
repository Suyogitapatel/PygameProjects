import pygame
import random

pygame.init()

# Choosen colors will be used to display the output 
white = [255, 255, 255]
lightpink = [255,182,193]
midnightblue = [25,25,112]
size = [400, 400]

# Specify the size
screen = pygame.display.set_mode(size)

# Caption for output window 
pygame.display.set_caption("Snowfall Window Screen")


snowFall = [] # Empty array for snowfall

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append([x, y])

# object to track time 
clock = pygame.time.Clock()

# Loop till the close button is pressed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                                
# Set the screen background
    screen.fill(white)

    for i in range(len(snowFall)):
        pygame.draw.circle(screen, midnightblue, snowFall[i], 2)

        snowFall[i][1] += 1
        if snowFall[i][1] > 400:
            y = random.randrange(-50, -10)
            snowFall[i][1] = y

            x = random.randrange(0, 400)
            snowFall[i][1] = x
    pygame.display.flip()
    clock.tick(20)
pygame.quit()            


