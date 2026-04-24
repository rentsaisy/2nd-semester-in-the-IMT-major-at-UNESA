import pygame, sys, time
from collections import deque

pygame.init()
screen = pygame.display.set_mode((800, 400))
font = pygame.font.SysFont(None, 36)

queue = deque(["laporan.pdf", "tugas.docx", "foto.jpg"])

def draw():
    screen.fill((255,255,255))
    x = 50
    for item in queue:
        pygame.draw.rect(screen, (100,149,237), (x,150,120,50))
        text = font.render(item, True, (255,255,255))
        screen.blit(text, (x+5,165))
        x += 140

    pygame.draw.rect(screen, (0,0,0), (650,140,100,80))
    screen.blit(font.render("Printer", True, (255,255,255)), (655,170))
    pygame.display.flip()

clock = pygame.time.Clock()

while queue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    draw()
    pygame.time.wait(1000)

    queue.popleft()  # dequeue (print)

    clock.tick(60)