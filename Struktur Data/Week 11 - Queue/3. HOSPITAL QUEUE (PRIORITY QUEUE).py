import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800,400))
font = pygame.font.SysFont(None, 30)

queues = {
    0: ["Ani","Dedi"],
    1: ["Eka"],
    2: ["Citra"],
    3: ["Budi"]
}

colors = {
    0:(255,0,0),
    1:(255,165,0),
    2:(255,255,0),
    3:(0,255,0)
}

def draw():
    screen.fill((255,255,255))
    y = 50
    for level in range(4):
        x = 50
        for p in queues[level]:
            pygame.draw.rect(screen, colors[level], (x,y,100,40))
            screen.blit(font.render(p, True,(0,0,0)), (x+10,y+10))
            x += 120
        y += 80
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    draw()
    pygame.time.wait(1000)

    for level in range(4):
        if queues[level]:
            queues[level].pop(0)
            break