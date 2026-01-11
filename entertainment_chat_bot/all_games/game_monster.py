"""Міні гра"""

from random import randint
from time import sleep

def movement_points():
    for _ in range(3):
        for _ in range(3):
                sleep(0.3)
                print(".", end="", flush=True)
        sleep(0.3)
        print("\b\b\b   \b\b\b", end="", flush=True)

player_hp = 100
monster_hp = 100
print("          🤼‍♂️  БИТВА ПОЧАЛАСЯ  🤼‍♂️", end="", flush=True)
sleep(2)
count = 1

while player_hp > 0 and monster_hp > 0:
    print(f"\r                   Раунд {count}!")
    try:
        action_player = int(input("\nТвій хід! 1 - вдарити 🤜 або 2 - лікуватися 💊: ").strip())
    except ValueError:
        print("Невірний ввод🛑. Введіть число 1 чи 2")
        continue
    match action_player:
        case 1:
            x = randint(10, 20)
            monster_hp -= x
            movement_points()
            print(f"\rТи наніс монстру {x} втрат!👍")
            if monster_hp <= 0:
                print("🎉ПЕРЕМОГА! Монстр повалений!🎉")
                break
        case 2:
                y = randint(20, 30)
                player_hp += y
                movement_points()
                print(f"\rТи випив ліки та відновив здоров'я на {y} HP🔝")
                if player_hp > 100:
                    player_hp = 100
                    print("HP не може бути більше 100! Ваше здоров'я 100!")
        case _:
            print("Невідома команда! Введіть 1 чи 2!")
            continue
    print("-"*10)
    sleep(1)
    print("Хід монстра! 👾")
    movement_points()
    i = randint(1, 5)
    if i == 3:
        z = randint(15, 30)
    else:
        z = randint(10, 20)
    player_hp -= z
    print(f"\rМонстр наніс тобі {z} втрат! 🩸")
    print("-"*10)
    if player_hp <= 0:
        print("GAME OVER. Ти загинув...😵")
        break
    print(f"Кінець раунда!\nТвій HP: {player_hp} | HP Монстра: {monster_hp}")
    print(f"Загрузка", end="", flush=True)
    movement_points()
    count += 1