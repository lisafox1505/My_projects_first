import pygame

pygame.init()

pygame.display.set_caption("Millionaire")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#Завантаження лого, або пустий квадрат
try:
    logo = pygame.image.load("logo.png").convert_alpha()
    logo_small = pygame.transform.scale(logo, (200, 200))
except:
    logo_small = pygame.Surface((200, 200)) # Пустой квадрат, если нет картинки
    logo_small.fill((0, 0, 100))

#Шріфти
FONT_Q = pygame.font.SysFont("Arial", 28)
FONT_ANS = pygame.font.SysFont("Arial", 18)
FONT_NAME_WIN = pygame.font.SysFont("Arial", 26)

#Кольори
DARK_BLUE_BG = (0, 0, 50)
BUTTON_FILL_COLOR = (0, 0, 47)
BUTTON_BORDER_COLOR = (0, 150, 255)
TEXT_COLOR = (245, 255, 250)
NAME_WIN_COLOR = (255, 215, 0)
WINS_COLORS_RECT = (255, 255, 255)
SUMA_SELECTOR_COLOR = (255, 140, 0)
HINT_COLOR = (135, 206, 235)
HINT_TEXT_COLOR = (25, 25, 112)

#Координати питання відповіді підказки
RECT_Q = pygame.Rect(70, 260, 660, 80)
BORDER_Q = pygame.Rect(50, 250, 700, 100)

RECT_A = pygame.Rect(105, 410, 260, 40)
BORDER_A = pygame.Rect(85, 400, 300, 60)

RECT_B = pygame.Rect(105, 500, 260, 40)
BORDER_B = pygame.Rect(85, 490, 300, 60)

RECT_C = pygame.Rect(435, 410, 260, 40)
BORDER_C = pygame.Rect(415, 400, 300, 60)

RECT_D = pygame.Rect(435, 500, 260, 40)
BORDER_D = pygame.Rect(415, 490, 300, 60)

RECT_H_1 = pygame.Rect(50, 150, 60, 40)
RECT_H_2 = pygame.Rect(50, 210, 60, 40)
RECT_H_3 = pygame.Rect(50, 230, 60, 40)
RECT_H_4 = pygame.Rect(50, 250, 60, 40)

#Суми виграшу, дані стану
PRIZES = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
step = 0

#Тексти питання відповіді
q_text = FONT_Q.render("Как правильно учить пайтон?", True, TEXT_COLOR)
a_text = FONT_ANS.render("A: Практиковаться", True, TEXT_COLOR)
b_text = FONT_ANS.render("B: Только смотреть видео", True, TEXT_COLOR)
c_text = FONT_ANS.render("C: Спать с книгой под подушкой", True, TEXT_COLOR)
d_text = FONT_ANS.render("D: Удалить PyCharm", True, TEXT_COLOR)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if step < 15:
                    step += 1

    screen.fill(DARK_BLUE_BG)

    #Інтерфейс
    screen.blit(logo_small, (300, 25))
    screen.blit(FONT_NAME_WIN.render("Name", True, NAME_WIN_COLOR), (50, 50))
    screen.blit(FONT_NAME_WIN.render(f"{PRIZES[step] if step > 0 else 0}", True, NAME_WIN_COLOR), (50, 100))

    #Суми виграшу прокрутка
    y_start = 20
    spacing = 22
    for i in PRIZES[9 + step::-1][:10]:
        color = NAME_WIN_COLOR if i in [1000, 32000, 1000000] else TEXT_COLOR
        win_text = FONT_ANS.render(f"{i}", True, color)
        text_rect = win_text.get_rect()
        text_rect.right = 750
        text_rect.top = y_start
        screen.blit(win_text, text_rect)
        y_start += spacing
    y_start_selector = 20
    if step < 6:
        selector_index = 9
    else:
        selector_index = 9 - (step - 6)

    # Рисуем каретку (оранжевый прямоугольник с закруглением)
    selector_y = y_start_selector + (selector_index * spacing)
    rect_coordinat = pygame.Rect(600, selector_y, 180, 20)
    pygame.draw.rect(screen, SUMA_SELECTOR_COLOR, rect_coordinat, border_radius=8, width=2)

#Прямокутники з питанням та варіантами відповіді
    pygame.draw.rect(screen, BUTTON_FILL_COLOR, RECT_Q)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, BORDER_Q, border_radius=30, width=2)
    screen.blit(q_text, q_text.get_rect(center=RECT_Q.center))

    pygame.draw.rect(screen, BUTTON_FILL_COLOR, RECT_A)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, BORDER_A, border_radius=20, width=2)
    screen.blit(a_text, a_text.get_rect(center=RECT_A.center))

    pygame.draw.rect(screen, BUTTON_FILL_COLOR, RECT_B)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, BORDER_B, border_radius=20, width=2)
    screen.blit(b_text, b_text.get_rect(center=RECT_B.center))

    pygame.draw.rect(screen, BUTTON_FILL_COLOR, RECT_C)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, BORDER_C, border_radius=20, width=2)
    screen.blit(c_text, c_text.get_rect(center=RECT_C.center))

    pygame.draw.rect(screen, BUTTON_FILL_COLOR, RECT_D)
    pygame.draw.rect(screen, BUTTON_BORDER_COLOR, BORDER_D, border_radius=20, width=2)
    screen.blit(d_text, d_text.get_rect(center=RECT_D.center))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()