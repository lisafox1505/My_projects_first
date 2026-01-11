import json

class UserMenu:
    def __init__(self, user_choice):
        self.user_choice = user_choice

    @classmethod
    def user_all_menu(cls, user_name):
        user_menu = (f"""
                {user_name}, виберіть дію:\n
                1 - Підбірка фільмів
                2 - Підбірка музики
                3 - Підбірка ігри
                4 - Анекдот
                5 - Цікавий факт
                6 - Вкусний рецепт
                7 - Загадка
                8 - Зіграти в міні-гру
                9 - Вийти
                """)
        return user_menu

    def open_file(self):
        try:
            with open(self.user_choice, "r", encoding="utf-8") as film_file:
                film_list = json.load(film_file)

                return film_list
        except FileNotFoundError:
            print("Помилка відкриття файлу. Спробуйте ще раз!")
            return []

class MediaSearcher:
    def __init__(self, json_path, text_category_name):
        self.json_path = json_path
        self.text_category_name = text_category_name
        self.result_list = []

    def creating_list_from_json(self):
        json_data = UserMenu(self.json_path)
        data_list = json_data.open_file()
        return data_list

    def prity_print(self):
        if isinstance(self.result_list, str):
            print(self.result_list)
            return
        if self.result_list and len(self.result_list) > 0:
            print("\nРезультат:")
            for i, n in enumerate(self.result_list, 1):
                print(f"{i}. {n}")
        else:
            print("Не знайдено!")

    def run(self):
        data_list = self.creating_list_from_json()
        while True:
            self.result_list = []
            selection_method = input(f"\nПідбірка {self.text_category_name} - 1\nПідбірка рік - 2\nВихід - 3\nВаш вибір: ")
            if selection_method == "1":
                user_choise = input(f"\nВведіть бажаний {self.text_category_name}: ").strip().lower()

                if self.text_category_name == "жанр":
                    for category in data_list:
                        if category.get("genre", "").lower() == user_choise:
                            self.result_list.append(category["title"])
                    self.prity_print()

                if self.text_category_name == "виконавець":
                    for category in data_list:
                        if category.get("artist", "").lower() == user_choise:
                            for cat in category["songs"]:
                                self.result_list.append(f"{cat['title']}({cat['year']})")
                    self.prity_print()

            elif selection_method == "2":
                user_year = input("Введіть бажаний рік: ").strip()
                if user_year.isdigit():
                    user_year = int(user_year)
                    for category in data_list:
                        if self.text_category_name == "виконавець":
                            for cat in category["songs"]:
                                if cat.get("year", "") == user_year:
                                    self.result_list.append(f"{cat['title']}({cat['year']})")
                        else:
                            if category.get("year", "") == user_year:
                                self.result_list.append(category["title"])
                    self.prity_print()
                else:
                    print("Будь ласка, вводьте тільки цифри!")
            elif selection_method == "3":
                break
            else:
                print("Невірний вибір!")

