import json
import random
import pygame


def questions_file_open():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            questions_data = json.load(file)
        random.shuffle(questions_data)
        return questions_data
    except FileNotFoundError:
        print("File not found.")
        return []

def next_question(questions_data, font_q, font_ans, text_color, rect_list, border_list ):
    if len(questions_data) > 0:
        current_question = questions_data.pop(0)
        question = current_question.get("question", "Помилка загрузки")
        options = current_question.get("options", ["Помилка загрузки"]*4)
        correct = current_question.get("correct", 0)
        q_text = font_q.render(question, True, text_color)
        answers_list = []
        for i in range(4):
            ans_text = font_ans.render(options[i], True, text_color)
            answers_list.append((rect_list[i], border_list[i], ans_text))
        return answers_list, q_text, correct, current_question
    return None


def hint_50_50(correct, answer_list_xy):
    answer_wrong_list = []
    result_list = []
    two_filtered_answer = []
    for i in range(4):
        if correct != i:
            answer_wrong_list.append(i)
        else:
            result_list.append(i)
    result = random.choice(answer_wrong_list)
    result_list.append(result)
    for key, value in enumerate(answer_list_xy):
        if key in result_list:
            two_filtered_answer.append(value)
    return two_filtered_answer


def hint_audience_help(correct_index, answers_count):
    # Обязательно инициализируем пустые списки внутри функции!
    two_most_likely_answers = []
    two_least_likely_answers = []

    correct_percent = random.randint(51, 70)

    if answers_count == 2:
        for i in range(2):
            if i == correct_index:
                two_most_likely_answers.append(correct_percent)
            else:
                two_most_likely_answers.append(100 - correct_percent)

    elif answers_count == 4:
        remaining_percent = 100 - correct_percent
        for i in range(4):
            if i == correct_index:
                two_most_likely_answers.append(correct_percent)
            else:
                part = random.randint(0, remaining_percent)
                two_most_likely_answers.append(part)
                remaining_percent -= part

        if remaining_percent > 0:
            for i in range(4):
                if i != correct_index:
                    two_most_likely_answers[i] += remaining_percent
                    break

    return two_most_likely_answers, two_least_likely_answers

def button(screen, color, rect_xy, text):
    pygame.draw.rect(screen, color, rect_xy, border_radius=20)
    screen.blit(text, text.get_rect(center=rect_xy.center))

if __name__ == "__main__":
    pass