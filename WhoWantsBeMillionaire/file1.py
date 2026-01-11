import pygame

pygame.init()

pygame.display.set_caption("Millionaire")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((65, 105, 225))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()