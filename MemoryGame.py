import pygame
import random
import sys

# Setup & Configuration 
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Memory Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Colors
BG_COLOR = (30, 30, 45)
CELL_COLOR = (60, 60, 80)
BLUE = (66, 135, 245)
GREEN = (72, 199, 116)
RED = (235, 87, 87)

# Game Variables
grid_size = 4
cell_dim = 100
margin = 10
grid_offset_x = (WIDTH - (grid_size * (cell_dim + margin))) // 2
grid_offset_y = 150

level = 3
score = 0
pattern = []
user_selection = []
# Phases: "SHOW", "GUESS", "RESULT"
phase = "START" 

def generate_pattern(count):
    cells = [(r, c) for r in range(grid_size) for c in range(grid_size)]
    return random.sample(cells, count)

def get_cell_from_pos(pos):
    x, y = pos
    col = (x - grid_offset_x) // (cell_dim + margin)
    row = (y - grid_offset_y) // (cell_dim + margin)
    if 0 <= row < grid_size and 0 <= col < grid_size:
        return (row, col)
    return None

# Main Game Loop 
while True:
    screen.fill(BG_COLOR)
    
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and phase == "START":
            pattern = generate_pattern(level)
            user_selection = []
            phase = "SHOW"
            timer = pygame.time.get_ticks()

        if event.type == pygame.MOUSEBUTTONDOWN and phase == "GUESS":
            cell = get_cell_from_pos(event.pos)
            if cell and cell not in user_selection:
                user_selection.append(cell)
                if len(user_selection) == len(pattern):
                    phase = "RESULT"
                    timer = pygame.time.get_ticks()

    # Game Logic / Timing
    current_time = pygame.time.get_ticks()
    if phase == "SHOW" and current_time - timer > 1500: # Show for 1.5s
        phase = "GUESS"
    
    if phase == "RESULT" and current_time - timer > 2000: # Show result for 2s
        if sorted(user_selection) == sorted(pattern):
            score += 1
            level = min(level + 1, 16)
        else:
            score = 0
            level = 3
        phase = "START"

    # 3. Drawing
    # Draw Text
    title_txt = font.render(f"Level: {level} | Score: {score}", True, (255, 255, 255))
    screen.blit(title_txt, (20, 20))
    
    inst_map = {"START": "Press any key to START", "SHOW": "Memorize!", "GUESS": "Replicate the pattern", "RESULT": "Checking..."}
    inst_txt = font.render(inst_map[phase], True, (200, 200, 200))
    screen.blit(inst_txt, (WIDTH//2 - inst_txt.get_width()//2, 80))

    # Draw Grid
    for r in range(grid_size):
        for c in range(grid_size):
            rect = pygame.Rect(grid_offset_x + c*(cell_dim+margin), grid_offset_y + r*(cell_dim+margin), cell_dim, cell_dim)
            color = CELL_COLOR
            
            if phase == "SHOW" and (r, c) in pattern:
                color = BLUE
            elif phase == "GUESS" and (r, c) in user_selection:
                color = BLUE
            elif phase == "RESULT":
                if (r, c) in pattern:
                    color = GREEN if (r, c) in user_selection else BLUE
                elif (r, c) in user_selection:
                    color = RED
            
            pygame.draw.rect(screen, color, rect, border_radius=8)

    pygame.display.flip()
    clock.tick(60)