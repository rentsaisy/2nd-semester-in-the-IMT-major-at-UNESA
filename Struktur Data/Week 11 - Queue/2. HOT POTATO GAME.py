import pygame, sys, math
from collections import deque

pygame.init()
screen = pygame.display.set_mode((600,600))
font = pygame.font.SysFont(None, 30)

players = deque(["A","B","C","D","E"])
num = 3
angle_step = 360 // len(players)

def draw(active_index):
    screen.fill((255,255,255))
    cx, cy = 300,300
    radius = 200

    for i, p in enumerate(players):
        angle = math.radians(i * (360/len(players)))
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)

        color = (255,0,0) if i == active_index else (0,128,0)
        pygame.draw.circle(screen, color, (int(x),int(y)), 30)
        text = font.render(p, True, (255,255,255))
        screen.blit(text, (int(x)-10,int(y)-10))

    pygame.display.flip()

while len(players) > 1:
    for i in range(num):
        players.append(players.popleft())
        draw(len(players)-1)
        pygame.time.wait(500)

    players.popleft()  # eliminated
    pygame.time.wait(800)

pygame.quit()