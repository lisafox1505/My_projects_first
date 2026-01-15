import pygame

#Кольори
DARK_BLUE_BG = (0, 0, 50)
BUTTON_FILL_COLOR = (0, 0, 47)
BUTTON_BORDER_COLOR = (0, 150, 255)
TEXT_COLOR = (245, 255, 250)
NAME_WIN_COLOR = (255, 215, 0)
WINS_COLORS_RECT = (255, 255, 255)
SUMA_SELECTOR_COLOR = (255, 140, 0)
HINT_BUTTON_COLOR = (135, 206, 250)
HINT_TEXT_COLOR = (25, 25, 112)
CORRECT_ANSWER_COLOR = (0, 250, 154)
NOT_CORRECT_ANSWER_COLOR = (220, 20, 60)

#Координати питання відповіді
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

rect_list = [RECT_A, RECT_B, RECT_C, RECT_D]
border_list = [BORDER_A, BORDER_B, BORDER_C, BORDER_D]

#Координати підказок
HINT_BUTTON_1 = pygame.Rect(50, 150, 110, 30)
HINT_BUTTON_2 = pygame.Rect(50, 200, 110, 30)
HINT_BUTTON_3 = pygame.Rect(170, 150, 110, 30)
HINT_BUTTON_4 = pygame.Rect(170, 200, 110, 30)

#Координати меню
RECT_WELC_1 = pygame.Rect(300, 350, 200, 30)
RECT_WELC_2 = pygame.Rect(300, 400, 200, 30)
RECT_WELC_3 = pygame.Rect(300, 450, 200, 30)
RECT_WELC_4 = pygame.Rect(300, 500, 200, 30)

# Координати вікон ввод ім'я, інформація, 2 видів кнопки виходу
RECT_NAME = pygame.Rect(200, 300, 400, 50)
INFO_RECT = pygame.Rect(50, 250, 700, 250)
RECT_QUIT = pygame.Rect(640, 520, 110, 30)
RECT_QUIT_IN_INPUT_NAME = pygame.Rect(510, 520, 110, 30)

PRIZES = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

RULES_TEXT = [
    "МЕТА ГРИ:",
    "Дати правильні відповіді на 15 запитань з різних галузей знань. "
    "Головний приз: 1 000 000 віртуальних гривень.",
    "",
    "ПРАВИЛА ТА ПІДКАЗКИ:",
    "• Варіанти відповідей: 4 варіанти, з яких лише один є вірним.",
    "• У вас є три класичні допомоги: 50/50, Зал та Дзвінок.",
    "• Кожна підказка доступна лише один раз за гру!",
    "",
    "НЕСПАЛИМІ СУМИ:",
    "• 5-те питання: 1 000 гривень.",
    "• 10-те питання: 32 000 гривень.",
    "УВАГА: Якщо ви дасте неправильну відповідь, гра завершується. "
    "Ви забираєте останню досягнуту «неспалиму» суму."
]
