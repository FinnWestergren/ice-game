import pygame

import gridClass
pygame.init()

#python's variable declaration has no type requirement, which might get confusing
window = pygame.display.set_mode((800,800))
grey = (100,100,100)
red = (255, 0, 0)
white = (255,255,255)
#colors handled as tuples which is nice
gridColor = grey      

gameGrid = gridClass.grid()
gameGrid.create(20, 20, 20, gridColor, pygame)


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    window.fill(white)
    gameGrid.display(window)
    pygame.display.update()

pygame.quit()
quit()




