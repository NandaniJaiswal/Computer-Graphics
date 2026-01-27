import math
import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D_Transformation")

white = (255, 255, 255)
black = (0, 0, 0)

Cube_vertices = [(-50,-50,-50), (-50, 50, -50), (50, 50, -50), (50, -50, -50),
                 (-50, -50, 50), (-50, 50, 50), (50, 50, 50), (50, -50, 50)]

Cube_egdes = [(0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)]

def translate(vertices, tx, ty, tz):
    result = []
    for x, y, z in vertices:
        result.append((x + tx, y + ty, z + tz))
    return result

def rotate(vertices, angle):
    result = []
    rad = math.radians(angle)

    for x, y, z in vertices:
        z1 = z * math.cos(rad) - x * math.sin(rad)
        x1 = z * math.sin(rad) - x * math.cos(rad)
        result.append((x1, y, z1))
    return result

def scale(vertices, Sx, Sy, Sz):
    result = []
    for x, y, z in vertices:
        result.append((x * Sx, y * Sy, z * Sz))
    return result

def reflect(vertices, axis):
    result = []
    if axis == "x":
        for x, y, z in vertices:
            result.append((x, -y, -z))
    elif axis == "y":
        for x, y, z in vertices:
            result.append((-x, y, -z))
    elif axis == "z":
        for x, y, z in vertices:
            result.append((-x, -y, z))
    return result

def projection(points):
    x, y, z = points
    distance = 300
    scale_points = distance / (distance - z)
    screen_x = x + width // 2
    screen_y = -y + height // 2
    screen_x = screen_x * scale_points
    screen_y = screen_y * scale_points
    return (int(screen_x), int(screen_y))

def draw_cube(vertices):
    projected = []

    for v in vertices:
        projected.append(projection(v))

    for edge in Cube_egdes:
        start = projected[edge[0]]
        end = projected[edge[1]]
        pygame.draw.line(screen, white, start, end)

def main():
    screen.fill(black)

    original = Cube_vertices
    translated = translate(Cube_vertices, 100, 0, 0)
    rotated = rotate(Cube_vertices, 10)
    scaling = scale(Cube_vertices, 20, 10, 10)
    reflection = reflect(Cube_vertices, "x")

    draw_cube(original)
    draw_cube(translated)
    draw_cube(rotated)
    draw_cube(scaling)
    draw_cube(reflection)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()