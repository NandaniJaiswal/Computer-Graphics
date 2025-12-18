import pygame
import sys
pygame.init()
width, height = 800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("DDA ALGORITHM")
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

def dda_algorithm (a, b, c, d):
    dx=c-a
    dy=d-b
    if (dx>dy):
        step=dx 
    else:
        step=dy
    xinc=dx/step
    yinc=dy/step
    x=a
    y=b 

    for i in range(step):
        x=x+xinc 
        y=y+yinc 
        screen.set_at((round(x),round(y)),WHITE)  


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.quit()
        screen.fill(BLACK)
        dda_algorithm(20, 20, 400, 400)
        pygame.display.flip()

if __name__ == "__main__":                          
    main()    

