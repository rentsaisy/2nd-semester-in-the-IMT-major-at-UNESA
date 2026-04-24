import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((800,400))
font = pygame.font.SysFont(None, 28)

queue = []
agents = [None, None]  # 2 agents

def draw():
    screen.fill((255,255,255))

    # queue
    x = 50
    for p in queue:
        pygame.draw.rect(screen, (0,128,255), (x,250,50,50))
        x += 60

    # agents
    for i in range(len(agents)):
        y = 100
        pygame.draw.rect(screen, (0,0,0), (500+i*100,y,60,60))
        if agents[i]:
            screen.blit(font.render("P", True,(255,255,255)), (510+i*100,120))

    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    # random arrival
    if random.random() < 0.3:
        queue.append("P")

    # assign to agents
    for i in range(len(agents)):
        if agents[i] is None and queue:
            agents[i] = queue.pop(0)

    # finish service randomly
    for i in range(len(agents)):
        if agents[i] and random.random() < 0.1:
            agents[i] = None

    draw()
    pygame.time.wait(500)
    clock.tick(60)