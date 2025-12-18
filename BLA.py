import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham's Line Algorithm")

white = (255, 255, 255)
black = (0, 0, 0)

# Taking two points from user
print("Enter the first point (x1, y1):")
x1 = int(input())
y1 = int(input())

print("Enter the second point (x2, y2):")
x2 = int(input())
y2 = int(input())

def line_generation(x1, y1, x2, y2):
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
            screen.set_at((x, y), white)
            x = x + x_inc
            if p >= 0:
                y =y + y_inc
                p = p + 2*dy - 2*dx
            else:
                p = p + 2*dy
    else:
        p = 2 * dx - dy
        for i in range(dy + 1):
            screen.set_at((x, y), white)
            y += y_inc
            if p >= 0:
                x = x + x_inc
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx

def main():
    screen.fill(black)
    line_generation(x1, y1, x2, y2)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()