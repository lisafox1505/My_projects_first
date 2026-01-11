import pygame

pygame.init()

pygame.display.set_caption("Millionaire")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
logo = pygame.image.load("logo.png").convert_alpha()
logo_small = pygame.transform.scale(logo, (200, 200))

FONT_Q = pygame.font.SysFont("Arial", 28)
FONT_ANS = pygame.font.SysFont("Arial", 18)

DARK_BLUE_BG = (0, 0, 50)
BUTTON_FILL = (0, 0, 40)
BUTTON_BORDER = (0, 150, 255)
TEXT_COLOR = (245, 255, 250)

RECT_Q = (70, 260, 660, 80)
BORDER_Q = (50, 250, 700, 100)

RECT_A = (105, 410, 260, 40)
BORDER_A = (85, 400, 300, 60)

RECT_B = (105, 500, 260, 40)
BORDER_B = (85, 490, 300, 60)

RECT_C = (435, 410, 260, 40)
BORDER_C = (415, 400, 300, 60)

RECT_D = (435, 500, 260, 40)
BORDER_D = (415, 490, 300, 60)

q_text = FONT_Q.render("Как правильно учить пайтон?", True, TEXT_COLOR)
a_text = FONT_ANS.render("A: Практиковаться", True, TEXT_COLOR)
b_text = FONT_ANS.render("B: Только смотреть видео", True, TEXT_COLOR)
c_text = FONT_ANS.render("C: Спать с книгой под подушкой", True, TEXT_COLOR)
d_text = FONT_ANS.render("D: Удалить PyCharm", True, TEXT_COLOR)

PRIZES = [100, 200, 500, 1000, 2000, 5000, 10000, 20000, 30000, 50000, 75000, 150000, 250000, 500000, 1000000]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(DARK_BLUE_BG)
    screen.blit(logo_small, (300, 25))

    pygame.draw.rect(screen, BUTTON_FILL, pygame.Rect(RECT_Q))
    pygame.draw.rect(screen, BUTTON_BORDER, pygame.Rect(BORDER_Q), border_radius=30, width=2)
    screen.blit(q_text, (70, 260))

    pygame.draw.rect(screen, BUTTON_FILL, pygame.Rect(RECT_A))
    pygame.draw.rect(screen, BUTTON_BORDER, pygame.Rect(BORDER_A), border_radius=20, width=2)
    screen.blit(a_text, (105, 410))

    pygame.draw.rect(screen, BUTTON_FILL, pygame.Rect(RECT_B))
    pygame.draw.rect(screen, BUTTON_BORDER, pygame.Rect(BORDER_B), border_radius=20, width=2)
    screen.blit(b_text, (105, 500))

    pygame.draw.rect(screen, BUTTON_FILL, pygame.Rect(RECT_C))
    pygame.draw.rect(screen, BUTTON_BORDER, pygame.Rect(BORDER_C), border_radius=20, width=2)
    screen.blit(c_text, (435, 410))

    pygame.draw.rect(screen, BUTTON_FILL, pygame.Rect(RECT_D))
    pygame.draw.rect(screen, BUTTON_BORDER, pygame.Rect(BORDER_D), border_radius=20, width=2)
    screen.blit(d_text, (435, 500))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()