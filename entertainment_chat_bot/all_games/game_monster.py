from random import randint
from time import sleep

from art import text2art
from colorama import init, Fore, Style
init()

def movement_points():
    for _ in range(3):
        for _ in range(3):
                sleep(0.3)
                print(".", end="", flush=True)
        sleep(0.3)
        print("\b\b\b   \b\b\b", end="", flush=True)

player_hp = 100
monster_hp = 100
print(Fore.BLUE + "          🤼‍♂️  БИТВА ПОЧАЛАСЯ  🤼‍♂️" + Style.RESET_ALL, end="", flush=True)
sleep(2)
count = 1
drag = 3

while player_hp > 0 and monster_hp > 0:

    print(Fore.BLUE + f"\r                   Раунд {count}!" + Style.RESET_ALL)

    try:
        action_player = int(input(Fore.GREEN + "\nТвій хід! " + Style.RESET_ALL + f"1 - вдарити 🤜 , 2 - лікуватися (у вас {drag}-💊), 3 - закінчити гру: ").strip())

    except ValueError:
        print(Fore.RED + "Невірний ввод🛑. Введіть число 1 чи 2" + Style.RESET_ALL)
        continue

    match action_player:

        case 1:
            x = randint(10, 20)
            monster_hp -= x
            movement_points()
            print(f"\rТи наніс монстру {Fore.GREEN + str(x) + Style.RESET_ALL} втрат!👍")

            if monster_hp <= 0:
                print(Fore.GREEN + text2art("YOU WIN") + "\n🎉Монстр повалений!🎉" + Style.RESET_ALL)
                break

        case 2:
            if drag > 0:
                y = randint(20, 30)
                player_hp += y
                movement_points()
                drag -= 1
                print(f"\rТи випив ліки та відновив здоров'я на {Fore.GREEN + str(y) + Style.RESET_ALL} HP🔝")

                if player_hp > 100:
                    player_hp = 100
                    print(Fore.RED + "HP не може бути більше 100!" + Style.RESET_ALL + " Ваше здоров'я 100!")

            else:
                print(Fore.RED + "Ліки закінчились😯. Ви втратила хід!" + Style.RESET_ALL)

        case 3:
            print(Fore.BLUE + "Дуже шкода! До нових зустрічей" + Style.RESET_ALL)
            break

        case _:
            print(Fore.RED + "Невідома команда! Введіть 1 чи 2!" + Style.RESET_ALL)
            break

    print("-"*10)
    sleep(1)
    print(Fore.RED + "Хід монстра! 👾" + Style.RESET_ALL)
    movement_points()
    i = randint(1, 5)

    if i == 3:
        z = randint(15, 30)

    else:
        z = randint(10, 20)

    player_hp -= z
    print(f"\rМонстр наніс тобі {Fore.RED + str(z) + Style.RESET_ALL} втрат! 🩸")
    print("-"*10)

    if player_hp <= 0:
        print(Fore.RED + text2art("GAME OVER") + "\nТи загинув...😵" + Style.RESET_ALL)
        break

    print(Fore.BLUE + f"Кінець раунда!" + Style.RESET_ALL + Fore.GREEN + "\nТвій HP: " + Style.RESET_ALL
          + f"{player_hp} | " + Fore.RED + "HP Монстра: " + Style.RESET_ALL + f"{monster_hp}")
    print(f"Загрузка", end="", flush=True)
    movement_points()
    count += 1