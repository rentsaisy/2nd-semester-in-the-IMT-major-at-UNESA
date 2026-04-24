import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,400))
font = pygame.font.SysFont(None, 30)

graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":[],
    "D":[],
    "E":[]
}

positions = {
    "A":(300,50),
    "B":(200,150),
    "C":(400,150),
    "D":(150,300),
    "E":(250,300)
}

visited = set()
queue = ["A"]

def draw(current=None):
    screen.fill((255,255,255))
    for node, pos in positions.items():
        color = (255,0,0) if node == current else (0,128,255)
        if node in visited:
            color = (0,255,0)
        pygame.draw.circle(screen, color, pos, 25)
        screen.blit(font.render(node, True,(0,0,0)), (pos[0]-10,pos[1]-10))
    pygame.display.flip()

while queue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    node = queue.pop(0)
    visited.add(node)
    draw(node)
    pygame.time.wait(1000)

    for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)