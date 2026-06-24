import random
import pygame
from functions import questions_file_open, hint_50_50, next_question, button, hint_audience_help
import constans as con


#Ініціалізація
pygame.init()
pygame.display.set_caption("Millionaire")
screen = pygame.display.set_mode((800, 600))

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

#Шріфти
FONT_Q = pygame.font.SysFont("Arial", 28)
FONT_ANS = pygame.font.SysFont("Arial", 18)
FONT_NAME_WIN = pygame.font.SysFont("Arial", 26)
FONT_INFO = pygame.font.SysFont("Arial", 15)
FONT_END_TITLE = pygame.font.SysFont("Arial", 42)
FONT_END_RESULT = pygame.font.SysFont("Arial", 28)
FONT_END_HINT = pygame.font.SysFont("Arial", 20)

# Тексти підказки та почати гру
hint_text_1 = FONT_ANS.render("50/50", True, con.HINT_TEXT_COLOR)
hint_text_2 = FONT_ANS.render("Дзвінок другу", True, con.HINT_TEXT_COLOR)
hint_text_3 = FONT_ANS.render("Допомога залу", True, con.HINT_TEXT_COLOR)
hint_text_4 = FONT_ANS.render("Вихід", True, con.HINT_TEXT_COLOR)
start_game_text = FONT_ANS.render("Почати", True, con.HINT_TEXT_COLOR)

# Тексти меню, правила
welc_text_1 = FONT_NAME_WIN.render("Новий гравець", True, con.HINT_TEXT_COLOR)
welc_text_2 = FONT_NAME_WIN.render("Продовжити", True, con.HINT_TEXT_COLOR)
welc_text_3 = FONT_NAME_WIN.render("Інформація", True, con.HINT_TEXT_COLOR)
welc_text_4 = FONT_NAME_WIN.render("Вихід", True, con.HINT_TEXT_COLOR)

# Тексти кінця гри
end_text_loss_title = FONT_END_TITLE.render("ГРА ЗАКІНЧЕНА!", True, con.SUMA_SELECTOR_COLOR)
end_text_loss_hint = FONT_END_HINT.render("Не здавайтеся! Спробуйте ще раз", True, con.TEXT_COLOR)
end_text_win_title = FONT_END_TITLE.render("ВІТАЄМО!", True, con.SUMA_SELECTOR_COLOR)
end_text_win_result = FONT_END_RESULT.render(f"ВИ — МІЛЬЙОНЕР!", True, con.TEXT_COLOR)
end_text_win_1000000 = FONT_END_TITLE.render("1 000 000 грн", True, con.SUMA_SELECTOR_COLOR)

#Дані стану
state = "WELCOME"
step = 0
win_suma = 0
q_text = None
is_answered = False
is_correct_answer = False
selected_button = None

button50_50_state = False
button_help_friend_state = False
button_help_audience_state = False
friend_hint_answer = ()
two_most_likely_answers = []
two_least_likely_answers = []
answers_list_with_50_50 = []

answer_time = 0
user_name = ""

value50_50 = ""
value_help_friend = ""
value_help_audience = ""

answers_list = []
correct = 0
all_questions = questions_file_open()


# Список для малювання підказок
hints_list = [
    (con.HINT_BUTTON_1, hint_text_1),
    (con.HINT_BUTTON_2, hint_text_2),
    (con.HINT_BUTTON_3, hint_text_3),
    (con.HINT_BUTTON_4, hint_text_4)
]

# Список для малювання кнопок меню
welc_button_list = [
    (con.RECT_WELC_1, welc_text_1),
    (con.RECT_WELC_2, welc_text_2),
    (con.RECT_WELC_3, welc_text_3),
    (con.RECT_WELC_4, welc_text_4),
]

#Завантаження лого, або пустий квадрат
try:
    logo_small = pygame.transform.scale(pygame.image.load("logo.png").convert_alpha(), (200, 200))
except Exception as e:
    print("Логотип не завантажен:", e)
    logo_small = pygame.Surface((200, 200))
    logo_small.fill((0, 0, 100))

running = True
while running:
# Функціонал кнопок
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "WELCOME":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Работа кнопок привітання
                if con.RECT_WELC_1.collidepoint(event.pos):
                    state = "NAME_INPUT"
                    value50_50 = ""
                    value_help_friend = ""
                    value_help_audience = ""
                    button50_50_state = False
                    button_help_friend_state = False
                    button_help_audience_state = False
                    user_name = ""
                    friend_hint_answer = ()
                    two_most_likely_answers = []
                    two_least_likely_answers = []
                    win_suma = 0

                elif con.RECT_WELC_2.collidepoint(event.pos):
                    if user_name == "":
                        state = "NAME_INPUT"
                    else:
                        state = "GAME"

                elif con.RECT_WELC_3.collidepoint(event.pos):
                    state = "INFORMATION"

                elif con.RECT_WELC_4.collidepoint(event.pos):
                    running = False

        elif state == "NAME_INPUT":
            # Кнопки почати гру та виходу
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and con.RECT_QUIT_IN_INPUT_NAME.collidepoint(event.pos):
                state = "WELCOME"
                user_name = ""

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and con.RECT_QUIT.collidepoint(event.pos):
                if len(user_name) > 0:
                    if q_text is None:
                        all_questions = questions_file_open()
                        result = next_question(all_questions, FONT_Q, FONT_ANS, con.TEXT_COLOR, con.rect_list, con.border_list)
                        if result:
                            answers_list, q_text, correct, current_question = result
                    state = "GAME"

            # Набор на клавіатурі ім'я
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]

                else:
                    if event.unicode.isprintable():
                        if len(user_name) < 15:
                            user_name += event.unicode

        elif state == "INFORMATION":
            # Кнопка виходу
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and con.RECT_QUIT.collidepoint(event.pos):
                state = "WELCOME"

        elif state == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Кнопки підказок та виходу
                if con.HINT_BUTTON_1.collidepoint(event.pos) and button50_50_state == False:
                    value50_50 = "50/50"
                    button50_50_state = True
                    answers_list_with_50_50 = hint_50_50(correct, answers_list)

                if con.HINT_BUTTON_2.collidepoint(event.pos) and button_help_friend_state == False:
                    value_help_friend = "Дзвінок другу"
                    button_help_friend_state = True

                    if value50_50 == "50/50" and answers_list_with_50_50:
                        friend_hint_answer = random.choice(answers_list_with_50_50)
                    else:
                        two_answer_for_help = hint_50_50(correct, answers_list)
                        friend_hint_answer = random.choice(two_answer_for_help)

                if con.HINT_BUTTON_3.collidepoint(event.pos) and button_help_audience_state == False:
                    value_help_audience = "Допомога зала"
                    button_help_audience_state = True

                    if value50_50 == "50/50" and answers_list_with_50_50:
                        correct_idx_50_50 = 0 if answers_list_with_50_50[0][0] == con.rect_list[correct] else 1
                        two_most_likely_answers = hint_audience_help(correct_idx_50_50, 2)[0]
                    else:
                        two_most_likely_answers, two_least_likely_answers = hint_audience_help(correct, 4)

                if con.HINT_BUTTON_4.collidepoint(event.pos):
                    state = "WELCOME"

                # Кнопки варіантів відповідей
                current_answer_list_for_buttons = answers_list_with_50_50 if value50_50 == "50/50" else answers_list
                for button_rect, border, text in current_answer_list_for_buttons:

                    if button_rect.collidepoint(event.pos) and not is_answered:
                        is_answered = True
                        answer_time = pygame.time.get_ticks()
                        selected_button = button_rect

                        if button_rect == con.rect_list[correct]:
                            is_correct_answer = True
                        else:
                            is_correct_answer = False

        elif state == "WIN":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and con.RECT_QUIT.collidepoint(event.pos):
                state = "WELCOME"
                user_name = ""
                win_suma = 0
                step = 0
                q_text = None
                is_answered = False
                is_correct_answer = False
                selected_button = None

                button50_50_state = False
                button_help_friend_state = False
                button_help_audience_state = False
                friend_hint_answer = ()
                two_most_likely_answers = []
                two_least_likely_answers = []

        elif state == "LOSS":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and con.RECT_QUIT.collidepoint(event.pos):
                state = "WELCOME"
                user_name = ""
                win_suma = 0
                step = 0
                q_text = None
                is_answered = False
                is_correct_answer = False
                selected_button = None

                button50_50_state = False
                button_help_friend_state = False
                button_help_audience_state = False
                friend_hint_answer = ()
                two_most_likely_answers = []
                two_least_likely_answers = []

# Малювання
    screen.fill(con.DARK_BLUE_BG)
    screen.blit(logo_small, (300, 25))

    #Вікно привітання
    if state == "WELCOME":
        for button_rect, text in welc_button_list:
            button(screen, con.HINT_BUTTON_COLOR, button_rect, text)

    # Вікно ввода ім'я
    if state == "NAME_INPUT":
        name_welc = FONT_NAME_WIN.render(user_name, True, con.TEXT_COLOR)
        pygame.draw.rect(screen, con.HINT_BUTTON_COLOR, con.RECT_NAME, border_radius=20, width=2),
        screen.blit(name_welc, name_welc.get_rect(center=con.RECT_NAME.center))

        # Кнопка почати гру та вихід
        button(screen, con.HINT_BUTTON_COLOR, con.RECT_QUIT, start_game_text)
        button(screen, con.HINT_BUTTON_COLOR, con.RECT_QUIT_IN_INPUT_NAME, hint_text_4)

    # Вікно інформації
    if state == "INFORMATION":
        pygame.draw.rect(screen, con.HINT_BUTTON_COLOR, con.INFO_RECT, border_radius=20)
        current_y = con.INFO_RECT.top + 17
        for line_str in con.RULES_TEXT:
            line_text = FONT_INFO.render(line_str, True, con.HINT_TEXT_COLOR)
            line_rect = line_text.get_rect(midtop=(con.INFO_RECT.centerx, current_y))

            screen.blit(line_text, line_rect)
            current_y += 17

        # Кнопка виходу
        button(screen, con.HINT_BUTTON_COLOR, con.RECT_QUIT, hint_text_4)

    # Інтерфейс гри
    if state == "GAME":
        screen.blit(FONT_NAME_WIN.render(user_name, True, con.NAME_WIN_COLOR), (50, 50))
        screen.blit(FONT_NAME_WIN.render(f"{con.PRIZES[step] if step > 0 else 0}", True, con.NAME_WIN_COLOR), (50, 100))

        # Кнопки підказок
        for i, (hint_button, hint_text) in enumerate(hints_list):
            if i == 0 and button50_50_state:
                continue
            elif i == 1 and button_help_friend_state:
                continue
            elif i == 2 and button_help_audience_state:
                continue
            button(screen, con.HINT_BUTTON_COLOR, hint_button, hint_text)

        #Суми виграшу прокрутка
        y_start = 20
        spacing = 22
        for i in con.PRIZES[9 + step::-1][:10]:
            color = con.NAME_WIN_COLOR if i in [1000, 32000, 1000000] else con.TEXT_COLOR
            win_text = FONT_ANS.render(f"{i}", True, color)
            text_rect = win_text.get_rect()
            text_rect.right = 750
            text_rect.top = y_start
            screen.blit(win_text, text_rect)
            y_start += 22
        y_start_selector = 20
        if step < 6:
            selector_index = 9
        else:
            selector_index = 9 - (step - 6)

        # Виділення виграшних сум
        selector_y = y_start_selector + (selector_index * spacing)
        rect_coordinates = pygame.Rect(600, selector_y, 180, 20)
        pygame.draw.rect(screen, con.SUMA_SELECTOR_COLOR, rect_coordinates, border_radius=8, width=2)

        # Прямокутники з питанням та варіантами відповіді
        button(screen, con.BUTTON_FILL_COLOR, con.RECT_Q, q_text)
        pygame.draw.rect(screen, con.BUTTON_BORDER_COLOR, con.BORDER_Q, border_radius=30, width=2)

        if value50_50 == "50/50" and answers_list_with_50_50:
            current_answer_list = answers_list_with_50_50
        else:
            current_answer_list = answers_list

        # УНІВЕРСАЛЬНИЙ ЦИКЛ МАЛЮВАННЯ КНОПОК
        for button_rect, border, text in current_answer_list:
            color = con.BUTTON_FILL_COLOR
            if is_answered:
                if button_rect == con.rect_list[correct]:
                    color = con.CORRECT_ANSWER_COLOR
                elif button_rect == selected_button:
                    color = con.NOT_CORRECT_ANSWER_COLOR

            border_color = con.BUTTON_BORDER_COLOR

            if value_help_friend == "Дзвінок другу" and friend_hint_answer:
                if button_rect == friend_hint_answer[0]:
                    border_color = con.SUMA_SELECTOR_COLOR

            button(screen, color, button_rect, text)
            pygame.draw.rect(screen, border_color, border, border_radius=30, width=2)

            if value_help_audience == "Допомога зала":
                if len(two_most_likely_answers) == 4:
                    idx_for_percent = answers_list.index((button_rect, border, text))
                else:
                    idx_for_percent = current_answer_list.index((button_rect, border, text))

                percent = two_most_likely_answers[idx_for_percent]
                percent_text = FONT_Q.render(str(percent) + "%", True, con.NAME_WIN_COLOR)
                screen.blit(percent_text, percent_text.get_rect(midright=(button_rect.right - 20, button_rect.centery)))


        if is_answered:
            current_time = pygame.time.get_ticks()
            if current_time - answer_time > 1500:
                if is_correct_answer:
                    step += 1
                    if 5 <= step < 10:
                        win_suma = 1000
                    elif 10 <= step < 15:
                        win_suma = 32000

                    if step < 15:
                        result = next_question(all_questions, FONT_Q, FONT_ANS, con.TEXT_COLOR, con.rect_list, con.border_list)
                        if result:
                            answers_list, q_text, correct, current_question = result
                            is_answered = False
                            selected_button = None
                            value50_50 = ""
                            value_help_friend = ""
                            value_help_audience = ""
                            friend_hint_answer = ()
                            two_most_likely_answers = []
                            two_least_likely_answers = []
                    else:
                        state = "WIN"
                else:
                    state = "LOSS"

    if state == "WIN":
        # Кнопка виходу
        button(screen, con.HINT_BUTTON_COLOR, con.RECT_QUIT, hint_text_4)

        screen.blit(end_text_win_title, end_text_win_title.get_rect(centerx=400, y=250))
        screen.blit(end_text_win_1000000, end_text_win_1000000.get_rect(centerx=400, y=350))
        screen.blit(end_text_win_result, end_text_win_result.get_rect(centerx=400, y=450))

    if state == "LOSS":
        # Кнопка виходу
        button(screen, con.HINT_BUTTON_COLOR, con.RECT_QUIT, hint_text_4)

        end_text_loss_result = FONT_END_RESULT.render(f"Ваш виграш: {win_suma} грн", True, con.TEXT_COLOR)
        screen.blit(end_text_loss_title, end_text_loss_title.get_rect(centerx=400, y=250))
        screen.blit(end_text_loss_result, end_text_loss_result.get_rect(centerx=400, y=350))
        screen.blit(end_text_loss_hint, end_text_loss_hint.get_rect(centerx=400, y=450))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()