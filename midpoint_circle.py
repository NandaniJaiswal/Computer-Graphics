import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Algorithm")

# Colors (RGB)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PINK   = (255, 105, 180)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BLACK  = (0, 0, 0)

# Input
x_center = 400  # center x
y_center = 300  # center y
r = 100         # radius

def plot_circle_points(xc, yc, x, y):
    screen.set_at((xc + x, yc + y), WHITE)
    screen.set_at((xc + x, yc - y), RED)
    screen.set_at((xc - x, yc + y), BLUE)
    screen.set_at((xc - x, yc - y), GREEN)
    screen.set_at((xc + y, yc + x), YELLOW)
    screen.set_at((xc + y, yc - x), PINK)
    screen.set_at((xc - y, yc + x), ORANGE)
    screen.set_at((xc - y, yc - x), PURPLE)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        plot_circle_points(xc, yc, x, y)
        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*(x - y) + 1

def main():
    screen.fill(BLACK)
    midpoint_circle(x_center, y_center, r)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
