import random
import os
import sys

from classes import UserMenu, MediaSearcher

def story_generator(data):
    all_stories = [value for d in data for value in d.values()]
    return random.choice(all_stories)

user_name = input("Введіть ваше ім'я: ")
all_menu = UserMenu.user_all_menu(user_name)

while True:
    try:
        print(all_menu)
        user_choise_menu = int(input("\nВведіть відповідну до вашого вибора цифру: "))
        if user_choise_menu == 1:
            result = MediaSearcher("data_file/films.json", "жанр")
            result.run()
        elif user_choise_menu == 2:
            result = MediaSearcher("data_file/music.json", "виконавець")
            result.run()
        elif user_choise_menu == 3:
            result = MediaSearcher("data_file/plays.json", "жанр")
            result.run()
        elif user_choise_menu == 4:
            json_data = UserMenu("data_file/jokes.json").open_file()
            result = story_generator(json_data)
            print(f"\nАнекдот:\n{result}")
        elif user_choise_menu == 5:
            json_data = UserMenu("data_file/storys.json").open_file()
            result = story_generator(json_data)
            print(f"\nЦікавий факт:\n{result}")
        elif user_choise_menu == 6:
            json_data = UserMenu("data_file/recipes.json").open_file()
            recipe = random.choice(json_data)
            print(f"\nБлюдо: {recipe['name']}")
            print(f"Інгредієнти: {', '.join(recipe['ingredients'])}")
            print(f"Спосіб приготування: {recipe['instructions']}")
        elif user_choise_menu == 7:
            json_data = UserMenu("data_file/riddles.json").open_file()
            riddle = random.choice(json_data)
            print(f"\nПитання: {riddle['question']}")
            n = 5
            while n > 0:
                answer = input(f"\nУ вас є {n} спроб! Введіть вашу відповідь, або 'off' щоб вийти: ").strip().lower()
                if answer == "off":
                    print(f"Відповідь: {riddle['answer']}")
                    break
                if riddle["answer"].lower() == answer:
                    print("🎉Вірно🎉")
                    break
                else:
                    print("Не вірно! Спробуйте ще раз")
                    n -= 1
        elif user_choise_menu == 8:
            os.system(f"{sys.executable} all_games/game_monster.py")

        elif user_choise_menu == 9:
            json_data = UserMenu("data_file/quotes.json").open_file()
            quot = random.choice(json_data)
            print(f"\nЦитата для Вас:\n{quot['text']}({quot['author']})")
            break
        else:
            print("Невірний ввод!")
    except ValueError:
        print("Можна ввести тільки цифру!")

