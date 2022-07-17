import sys
import pygame
import config as cf

from pygame import mixer


# initialize all pygame modules
pygame.init()

# setting the window dimension
window = pygame.display.set_mode([cf.WIDTH, cf.HEIGHT])

# adding label to the window
pygame.display.set_caption(cf.TITLE)

# setting font for the application
font = pygame.font.Font(cf.FONT, cf.FONTSIZE)

# setting clock 
timer = pygame.time.Clock()


# MAIN LOOP
while True:
    # specify for every seconds how many frames should pass
    timer.tick(cf.FPS)

    # setting the background of window
    window.fill(cf.BLACK)

    # loop to check for any type of event and do the needful
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # to update the screen
    pygame.display.flip()

pygame.quit()
