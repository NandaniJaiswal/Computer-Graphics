import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Ellipse Algorithm")

# Colors 
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)

# Input
#x_center = 400  # center x
#y_center = 300  # center y

#rx = 100         # major axis
#ry = 60          # minor axis

print ("Enter the center points:")
x_center = int(input())
y_center = int(input())

print ("Enter the major and minor axes:")
rx = int(input())
ry = int(input())

def draw_ellipse(x_center, y_center, rx, ry):
    x = 0
    y = ry

    p1 = ry*ry-rx*rx*ry+0.25*rx*rx

    while (2*ry*ry*x <= 2*rx*rx*y):   #dx<=dy


        screen.set_at((x_center + x, y_center + y), "RED")
        screen.set_at((x_center + x, y_center - y), "BLUE")
        screen.set_at((x_center - x,y_center + y), "PURPLE")
        screen.set_at((x_center - x, y_center - y), "ORANGE")

        x = x+1
        if(p1<0):
            y=y
            p1=p1+2*ry*ry*x+ry*ry
        else:
            y=y-1
            p1=p1+2*ry*ry*x-2*rx*rx*y+ry*ry

        
    p2=ry*ry*x+0.5*x+0.5+rx*rx*y-1*y-1-rx*rx*ry*ry

    while y!=0:


        screen.set_at((x_center + x, y_center + y), "PINK")
        screen.set_at((x_center + x, y_center - y), "YELLOW")
        screen.set_at((x_center - x,y_center + y), "GREEN")
        screen.set_at((x_center - x, y_center - y), "WHITE")

        y=y-1
        if(p2>0):
             x=x
             p2=p2-2*rx*rx*y+rx*rx
        else:
             x=x+1
             p2=p2+2*ry*ry*x-2*rx*rx*y+rx*rx



def main():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_ellipse(x_center, y_center, rx ,ry)
        pygame.display.flip()       


if __name__ == "__main__":
    main()
