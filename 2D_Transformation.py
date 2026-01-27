import pygame
import sys
import math

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D_Transformation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

def line_generation(x1, y1, x2, y2,color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x2 > x1:
        x_inc = 1 
    else :
        x_inc = -1
    if y2 > y1:
        y_inc = 1 
    else:
        y_inc = -1

    x = x1
    y = y1

    if dx > dy:
        p = 2 * dy - dx
        for i in range(dx + 1):
            screen.set_at((x, y), color)
            x = x + x_inc
            if p >= 0:
                y =y + y_inc
                p = p + 2*dy - 2*dx
            else:
                p = p + 2*dy
    else:
        p = 2 * dx - dy
        for i in range(dy + 1):
            screen.set_at((x, y), color)
            y += y_inc
            if p >= 0:
                x = x + x_inc
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
def translate (x1,y1,x2,y2,tx,ty):
    return x1+tx, y1+ty, x2+tx, y2+ty

def scaling(x1,y1,x2,y2,sx,sy,cx,cy):
    xa=int(cx+sx*(x1-cx))
    ya=int(cy+sy*(y1-cy))
    xb=int(cx+sx*(x2-cx))
    yb=int(cy+sy*(y2-cy))

    return xa,ya,xb,yb

def reflection (x1,y1,x2,y2,axis,cx,cy):
    def reflect_point(x,y):
        x=x-cx
        y=y-cy
        if axis == 'x':
            y=-y
        elif axis == 'y':
            x=-x
        return x+cx , y+cy
    
    return reflect_point(x1,y1) + reflect_point(x2,y2) 

def rotation (x1,y1,x2,y2,angle,cx,cy):
    rad = math.radians(angle)

    def rotate_points(x,y):
        x -= cx
        y -= cy
        xr= x * math.cos(rad)-y * math.sin(rad)
        yr= x * math.sin(rad)+y * math.cos(rad)
        return int(xr + cx), int(yr+cy)

    return rotate_points(x1,y1) + rotate_points(x2,y2)

def main():
    
    angle=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        line_generation(100,50,60,80,WHITE)
        a,b,c,d=translate(100,50,60,80,20,30) 
        line_generation(a,b,c,d,GREEN)
        a,b,c,d=scaling(100,50,60,80,2,2,100,50)
        line_generation(a,b,c,d,YELLOW)
        a,b,c,d=reflection(100,50,60,80,'x',100,50)
        line_generation(a,b,c,d,BLUE)
        a,b,c,d=rotation(100,50,60,80,angle,100,50)
        angle= angle+1
        line_generation(a,b,c,d, RED)
        pygame.display.flip()
       

if __name__ == "__main__":
    main()        

