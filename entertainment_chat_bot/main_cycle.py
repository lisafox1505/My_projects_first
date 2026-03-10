import random
import os
import sys

import emoji
from art import text2art, art
from colorama import init, Fore, Style
init()

from classes import MenuManager, MediaSearcher


def story_generator(data):
    """
        Приймає список словників із бази даних.
        Повертає один випадковий елемент (анекдот або цікавий факт).
    """

    all_stories = [value for d in data for value in d.values()]
    return random.choice(all_stories)


def start_game(name_file):
    """
        Запускає зовнішній Python-файл із міні-грою за вказаним шляхом.
        У разі відсутності файлу виводить повідомлення про помилку.
    """

    if os.path.isfile(name_file):
        os.system(f"{sys.executable} {name_file}")
    else:
        print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)


texts_for_choice = {"кіно":
                          "\n\t\tБойовик, Фантастика, Мультфільм, Драма, Біографія"
                          "\n\t\tКомедія, Трилер, Фентезі, Жахи, Військовий"
                          "\n\t\tВестерн, Пригоди, Мюзикл, Детектив",
                    "виконавці":
                          "\n\t\tABBA, AC/DC, Adele, Bee Gees, Beyoncé, Billie Eilish"
                          "\n\t\tBon Jovi, Britney Spears, Bruno Mars, Coldplay"
                          "\n\t\tDaft Punk, Ed Sheeran, Eminem, Guns N' Roses"
                          "\n\t\tImagine Dragons, Justin Bieber, Katy Perry, Lady Gaga"
                          "\n\t\tLinkin Park, Madonna, Maroon 5, Metallica, Michael Jackson"
                          "\n\t\tNirvana, Queen, Red Hot Chili Peppers, Rihanna, Shakira"
                          "\n\t\tTaylor Swift, The Beatles, The Weeknd.",
                    "ігри":
                          "\n\t\tJRPG, MOBA, RPG, RPG / Екшн, RPG / Шутер"
                          "\n\t\tВестерн / Екшн, Виживання, Екшн, Екшн / RPG"
                          "\n\t\tЕкшн / Симулятор кур'єра, Жахи, Кооператив"
                          "\n\t\tКоролівська битва, Метроідванія, Перегони"
                          "\n\t\tПлатформер, Пригоди, Пригоди / Драма, Пісочниця"
                          "\n\t\tРитм-екшн, Роуглайк, Симулятор життя, Симулятор міста"
                          "\n\t\tСимулятор перегонів, Симулятор ферми, Слешер, Соціальна дедукція"
                          "\n\t\tСпорт, Спорт / Перегони, Стратегія, Стратегія / RPG, Файтинг, Шутер"
                    }


if __name__ == "__main__":

    user_name = input("Введіть ваше ім'я: ")
    all_menu = MenuManager.user_all_menu(user_name)


    while True:
        try:
            print(all_menu)
            user_choice_menu = int(input("Введіть відповідну до вашого вибору цифру: "))

            if user_choice_menu == 1:
                result = MediaSearcher("data_file/films.json", "жанр")
                result.run(texts_for_choice.get("кіно", " "))

            elif user_choice_menu == 2:
                result = MediaSearcher("data_file/music.json", "виконавець")
                result.run(texts_for_choice.get("виконавці", " "))

            elif user_choice_menu == 3:
                result = MediaSearcher("data_file/plays.json", "жанр")
                result.run(texts_for_choice.get("ігри", " "))

            elif user_choice_menu == 4:
                json_data = MenuManager("data_file/jokes.json").open_file()
                if json_data:
                    result = story_generator(json_data)
                    print("-" * 50)
                    print(Fore.GREEN + text2art("ANEKDOT"))
                    print(f"{result}\n")
                    print(art("happy") + Style.RESET_ALL)
                    print("-" * 50)

                else:
                    print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)

            elif user_choice_menu == 5:
                json_data = MenuManager("data_file/stories.json").open_file()
                if json_data:
                    result = story_generator(json_data)
                    print("-" * 50)
                    print(Fore.GREEN + "\t\t\t\t" + emoji.emojize(':thinking_face:')
                          + "Цікавий факт" + emoji.emojize(':thinking_face:')
                          + f"\n\n{result}"+ Style.RESET_ALL)
                    print("-" * 50)

                else:
                    print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)


            elif user_choice_menu == 6:
                json_data = MenuManager("data_file/recipes.json").open_file()
                if json_data:
                    recipe = random.choice(json_data)
                    print("-" * 50)
                    print(Fore.GREEN + f"\t\t\t\tБлюдо:\n{Fore.LIGHTWHITE_EX + recipe['name']}")
                    print(Fore.GREEN + f"\n\t\t\t\tІнгредієнти:\n{Fore.LIGHTWHITE_EX + ', '.join(recipe['ingredients'])}")
                    print(Fore.GREEN + f"\n\t\t\t\tСпосіб приготування:\n{Fore.LIGHTWHITE_EX + recipe['instructions']}" + Style.RESET_ALL)
                    print("-" * 50)

                else:
                    print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)

            elif user_choice_menu == 7:
                json_data = MenuManager("data_file/riddles.json").open_file()
                if json_data:
                    riddle = random.choice(json_data)
                    print("-" * 50)
                    print(Fore.GREEN + f"\t\t\t\tПитання:\n{Fore.LIGHTWHITE_EX + riddle['question']}" + Style.RESET_ALL)
                    n = 5

                    while n > 0:
                        answer = input(f"\nУ вас є {Fore.GREEN + str(n) + Style.RESET_ALL} спроб! Введіть вашу відповідь, або "
                                       + Fore.GREEN + 'off' + Style.RESET_ALL + " щоб вийти: ").strip().lower()
                        if answer == "off":
                            print(Fore.GREEN + f"\n\t\t\t\tВідповідь:\n{Fore.LIGHTWHITE_EX + riddle['answer']}" + Style.RESET_ALL)
                            break
                        if riddle["answer"].lower() == answer:
                            print(Fore.GREEN + emoji.emojize(":tada:") + text2art("BIPHO") + Style.RESET_ALL + emoji.emojize(":tada:"))
                            break

                        else:
                            print(Fore.RED + emoji.emojize(':crying_face:') + "Не вірно!"
                                  + emoji.emojize(':crying_face:') + Style.RESET_ALL)
                            n -= 1

                    else:
                        print(Fore.RED + emoji.emojize(':crying_face:') + "Нажаль ви не дали вірну відповідь"
                              + emoji.emojize(':crying_face:') + Style.RESET_ALL)
                        print(Fore.GREEN + f"\n\t\t\t\tВідповідь:\n{Fore.LIGHTWHITE_EX + riddle['answer']}" + Style.RESET_ALL)
                    print("-" * 50)

                else:
                    print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)

            elif user_choice_menu == 8:
                choice = input(Fore.BLUE + Style.BRIGHT +
                               "\n\t\t\t\t\tВиберіть гру:" +Fore.CYAN +
                               "\n\t\t\t\t1 - Битва з монстром"
                               "\n\t\t\t\t2 - Таблиця множення"
                               "\n\t\t\t\t3 - Пайтон - Казино"
                               "\n\t\t\t\t4 - В головне меню\n--> " + Style.RESET_ALL)

                if choice == "1":
                    start_game("all_games/game_monster.py")
                elif choice == "2":
                    start_game("all_games/math_trainer.py")
                elif choice == "3":
                    start_game("all_games/slot_machine.py")
                else:
                    continue

            elif user_choice_menu == 9:
                print(Fore.CYAN + "\n\t\t\t\tДОПОБАЧЕННЯ " + emoji.emojize(":grinning_face:") + Style.RESET_ALL)
                break

            else:
                print(Fore.RED + "Невірний ввод!" + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Можна ввести тільки цифру!" + Style.RESET_ALL)

