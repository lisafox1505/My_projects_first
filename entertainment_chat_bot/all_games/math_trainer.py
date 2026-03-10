import random
import threading
import time
from colorama import Fore, Style, init
from tqdm import tqdm

init()

text = [
    Fore.CYAN + Style.BRIGHT + "\n\t\t\t\t📜 ПЕРЕВІРИМО ЗНАННЯ ТАБЛИЦІ МНОЖЕННЯ? ПРАВИЛА ГРИ:",
    Fore.LIGHTWHITE_EX + "\t\t\t\t🧠 Я даю приклад — ти швидко пишеш відповідь.",
    Fore.YELLOW + "\t\t\t\t⏳ На кожен РАУНД у тебе є рівно 1 хвилина. Виріши якомога більше!",
    Fore.GREEN + "\t\t\t\t✅ Кожна правильна відповідь = +1 бал до загального рахунку.",
    Fore.RED + "\t\t\t\t❤️ Помилка або кінець часу — мінус 1 життя (всього їх 3 на всю гру).",
    Fore.MAGENTA + "\t\t\t\t📈 Попереду 10 раундів. Покажи свій максимум!",
    Fore.CYAN + Style.BRIGHT + "\t\t\t\t🎮 Готові випробувати себе? Поїхали!\n" + Style.RESET_ALL
]
for i in text:
    print(i)
    time.sleep(0.5)

rounds = 1
points = 0
live_count = 3
stop_play = False

def counting_time():
    time.sleep(60)

while not stop_play and rounds <= 10:
    print(Fore.CYAN + Style.BRIGHT + f"\n\t\t\t\t\t🎯 РАУНД {rounds} 🎯" + Style.RESET_ALL)
    thread = threading.Thread(target=counting_time)
    thread.daemon = True
    thread.start()
    start_time = time.time()


    while thread.is_alive():
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        x = a * b

        print(f"\n▶ {a} * {b} = ", end="")
        answer = input("")
        if thread.is_alive():
            if answer.isdigit():
                if x == int(answer):
                    points += 1
                    print(Fore.GREEN + f"   ✅ Правильно! Залишилось {round(60 - (time.time() - start_time))} сек ⏱️" + Style.RESET_ALL)
                else:
                    live_count -= 1
                    print(Fore.YELLOW + f"   ❌ Помилка! Мінус життя 💔. Залишилось: {live_count}" + Style.RESET_ALL)
                    if live_count == 0:
                        break
            else:
                print(Fore.RED + f"   ⚠️ Ввести можна тільки число!" + Style.RESET_ALL)
                live_count -= 1
                if live_count == 0:
                    break
                else:
                    print(Fore.YELLOW + f"   ❌ Мінус життя 💔. Залишилось: {live_count}")
                    print(f"   ⏱️ Залишилось {round(60 - (time.time() - start_time))} секунд" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"\n   ⏳ Час закінчився!" + Style.RESET_ALL)

    if live_count == 0:
        stop_play = True
        print(Fore.RED + Style.BRIGHT + f"\n💀 ГРА ЗАКІНЧЕНА 💀")
        print(f"📊 Пройдено раундів: {rounds} | 🏆 Вірних відповідей: {points}\n" + Style.RESET_ALL)
        break

    else:
        print(Fore.GREEN + Style.BRIGHT + f"\n✨ Раунд {rounds} завершено! Балів: {points}. Готуйся... ✨" + Style.RESET_ALL)
        choice = input(Fore.CYAN + Style.BRIGHT + "[1] - Продовжити чи [2] - закінчити гру?: "+ Style.RESET_ALL)
        if choice == "2":
            break
        else:
            print(Fore.GREEN + Style.BRIGHT + f"\nГотуйся... ✨" + Style.RESET_ALL)
            for _ in tqdm(range(100), colour="cyan", bar_format="   {bar}"):
                time.sleep(0.01)
            time.sleep(5)

    rounds += 1

print(Fore.CYAN + Style.BRIGHT + "\n\t\t\t\t🏆 ПІДСУМКИ ГРИ 🏆" + Style.RESET_ALL)

if points < 30:
    print(Fore.YELLOW + f"Твій результат: {points} балів. Новачок! Треба ще трохи потренуватися." + Style.RESET_ALL)
elif 30 <= points < 80:
    print(Fore.GREEN + f"Твій результат: {points} балів. Впевнений рівень! Добре знаєш таблицю." + Style.RESET_ALL)
elif 80 <= points < 150:
    print(Fore.MAGENTA + f"Твій результат: {points} балів. Профі! У тебе чудова швидкість реакції." + Style.RESET_ALL)
else:
    print(Fore.RED + Style.BRIGHT + f"Твій результат: {points} балів. ТИ ПРОСТО МАТЕМАТИЧНИЙ МОНСТР! 🔥" + Style.RESET_ALL)



