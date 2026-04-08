import pygame

pygame.init()

# Window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze BFS Shortest Path")

# Colors
BG = (10, 30, 60)
WALL = (20, 40, 80)
PATH = (240, 225, 180)
VISITED = (150, 230, 200)  # Cyan - being explored
FINAL = (50, 255, 100)  # Bright green - solution path
DEAD_END = (255, 150, 50)  # Bright orange - wrong path
WHITE_BLOCK = (230, 230, 230)

START_COLOR = (0, 200, 150)
END_COLOR = (255, 170, 0)

GRID = (30, 50, 90)

# Maze (adjusted like image)
maze = [
    list("###############"),
    list("#...#...#.....#"),
    list("###.#.#.#.###.#"),
    list("#.....#...#.#.#"),
    list("#.#######.#...#"),
    list("#.#.....#.#####"),
    list("#.#.###.#....##"),
    list("#...#.#.####.##"),
    list("###.#.#....#..#"),
    list("#.#.#.####.##.#"),
    list("#.#......#..#.#"),
    list("#.######.####.#"),
    list("#.....#.......#"),
    list("#####.#######E#"),
    list("###############")
]

ROWS = len(maze)
COLS = len(maze[0])
CELL = WIDTH // COLS

# Find start (first dot '.')
start = None
for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == '.':
            start = (i, j)
            break
    if start:
        break

# Draw
def draw():
    WIN.fill(BG)

    for i in range(ROWS):
        for j in range(COLS):
            x, y = j * CELL, i * CELL

            if maze[i][j] == '#':
                color = WALL
            elif maze[i][j] == 'E':
                color = END_COLOR
            elif maze[i][j] == 'x':
                color = VISITED
            elif maze[i][j] == 'o':
                color = FINAL
            elif maze[i][j] == 'v':
                color = DEAD_END
            else:
                color = PATH

            pygame.draw.rect(WIN, color, (x, y, CELL, CELL))
            pygame.draw.rect(WIN, GRID, (x, y, CELL, CELL), 1)

            # Draw symbols
            if maze[i][j] == 'x':
                pygame.draw.circle(WIN, (100, 255, 150), (x+CELL//2, y+CELL//2), 5)
            elif maze[i][j] == 'o':
                pygame.draw.circle(WIN, (0, 255, 50), (x+CELL//2, y+CELL//2), 5)
            elif maze[i][j] == 'v':
                pygame.draw.circle(WIN, (255, 100, 0), (x+CELL//2, y+CELL//2), 5)
            elif (i, j) == start:
                pygame.draw.circle(WIN, START_COLOR, (x+CELL//2, y+CELL//2), 6)

    pygame.display.update()

# BFS + find shortest path
def bfs():
    from collections import deque
    queue = deque([(start, [start])])
    visited = set([start])

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    running = True
    shortest_path = None

    while queue and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        (x, y), path = queue.popleft()

        if maze[x][y] == 'E':
            shortest_path = path
            print("Exit Found! Shortest path length:", len(path))
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if (nx, ny) not in visited and maze[nx][ny] in ['.', 'E']:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    if shortest_path:
        # draw shortest path with green color
        for px, py in shortest_path:
            if (px, py) != start:
                maze[px][py] = 'o'
            draw()
            pygame.time.delay(100)
        
        print("Animation completed!")

# Main
def main():
    running = True
    started = False

    while running:
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    bfs()
                    started = True

    pygame.quit()

main()