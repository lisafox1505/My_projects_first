import json
import time

from colorama import init, Fore, Style
from tqdm import tqdm

init()


class MenuManager:
    """Клас для керування меню та завантаження даних із JSON-файлів."""

    def __init__(self, file_path):
        self.file_path = file_path


    @staticmethod
    def user_all_menu(user_name):
        """Генерує та повертає відформатований текст головного меню чат-бота."""

        user_menu = (Fore.BLUE + Style.BRIGHT + f"""
                {user_name}, виберіть дію:\n"""+
                Fore.CYAN + f"""
                1 - Підбірка фільмів
                2 - Підбірка музики
                3 - Підбірка ігри
                4 - Анекдот
                5 - Цікавий факт
                6 - Смачний рецепт
                7 - Загадка
                8 - Зіграти в міні-гру
                9 - Вийти
                """  + Style.RESET_ALL)

        return user_menu


    def open_file(self):
        """Відкриває JSON файл та повертає його вміст. Обробляє помилку відсутності файлу."""

        try:
            with open(self.file_path, "r", encoding="utf-8") as film_file:
                film_list = json.load(film_file)
                return film_list

        except FileNotFoundError:
            print(Fore.RED + "Помилка відкриття файлу." + Style.RESET_ALL)
            return []


class MediaSearcher:
    """Клас для пошуку та гарного виведення медіаконтенту (фільми, музика, ігри)."""

    def __init__(self, json_path, text_category_name):
        self.json_path = json_path
        self.text_category_name = text_category_name
        self.result_list = []


    def creating_list_from_json(self):
        """Створює екземпляр MenuManager для отримання даних із зазначеного JSON-файлу."""

        json_data = MenuManager(self.json_path)
        data_list = json_data.open_file()
        return data_list


    def pretty_print(self, choice):
        """Виводить результати пошуку в консоль із використанням анімації завантаження (tqdm)."""

        if self.result_list and len(self.result_list) > 0:
            print("Шукаємо: ")
            for _ in tqdm(range(100), colour="cyan", bar_format="{bar}"):
                time.sleep(0.01)

            print("-" * 50)
            print(f"Ось що ми знайшли за запитом '{choice.upper()}':")
            for i, n in enumerate(self.result_list, 1):
                print(f"{i}. {Fore.BLUE + n}" + Style.RESET_ALL)
            print("-" * 50)

        else:
            for _ in tqdm(range(100), colour="cyan", bar_format="{bar}"):
                time.sleep(0.05)
            print(Fore.RED + "Не знайдено!" + Style.RESET_ALL)


    def run(self, text):
        """Основний цикл методу: запитує критерії пошуку у користувача та формує список результатів."""

        data_list = self.creating_list_from_json()
        if data_list:
            while True:
                self.result_list = []
                selection_method = input(Fore.CYAN + f"\n\t\t1 - Підбірка {self.text_category_name}\n\t\t2 - Підбірка рік\n\t\t3 - Вихід\n" + Style.RESET_ALL + "\nВаш вибір: ")
                if selection_method == "1":

                    if self.text_category_name == "жанр":
                        print(Fore.CYAN +
                              text
                              + Style.RESET_ALL)

                        user_choice = input(f"\nВведіть бажаний жанр зі списку: ").strip().lower()
                        for category in data_list:
                            if category.get("genre", "").lower() == user_choice:
                                self.result_list.append(category["title"])
                        self.pretty_print(user_choice)

                    if self.text_category_name == "виконавець":
                        print(Fore.CYAN +
                              text
                              + Style.RESET_ALL)

                        user_choice = input(f"\nВведіть бажаного виконавця зі списку: ").strip().lower()
                        for category in data_list:
                            if category.get("artist", "").lower() == user_choice:
                                for cat in category["songs"]:
                                    self.result_list.append(f"{cat['title']}({cat['year']})")
                        self.pretty_print(user_choice)

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
                        self.pretty_print(str(user_year))

                    else:
                        print(Fore.RED + "Будь ласка, вводьте тільки цифри!" + Style.RESET_ALL)

                elif selection_method == "3":
                    break

                else:
                    print(Fore.RED + "Невірний вибір!" + Style.RESET_ALL)

        else:
            print(Fore.RED + "Щось пішло не так! Спробуйте ще раз!" + Style.RESET_ALL)
