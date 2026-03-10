import random
import time

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"

slot_symbols = ["🍒", "🍋", "🔔", "💎", "🎰", "🍀", "7️⃣", "🍇", "🍉", "⭐", "🍒", "🍋", "🍀", "7️⃣", "💎", "🍇"]
symbols_dict = {"🍋": 10, "7️⃣": 50, "🍒": 15}

money_start = 100

print(f"{CYAN}{BOLD}=== 🎰 ЛАСКАВО ПРОСИМО ДО PYTHON CASINO 🎰 ==={RESET}")
print(f"{CYAN}Правила гри:{RESET}")
print(f"• 3 однакові символи '7️⃣' — {YELLOW}ДЖЕКПОТ (Ставка x50){RESET}")
print(f"• 3 однакові '🍒' — {GREEN}x15{RESET}, '🍋' — {GREEN}x10{RESET}, інші — {GREEN}x5{RESET}")
print(f"• Будь-які 2 однакові символи — {GREEN}Втішний приз (Ставка x2){RESET}")
print(f"• Всі різні — втрата ставки.")
print(f"{CYAN}=============================================={RESET}\n")

while True:
    print(f"Поточний баланс: {YELLOW}{BOLD}{money_start} ₴{RESET}")
    choice = input(f"{CYAN}Виберіть дію: [1] Грати  [2] Забрати гроші та вийти ➔ {RESET}")
    if choice == "1":
        bet = input("Введіть ставку: ")
        if bet.isdigit() and int(bet) > 0:
            bet = int(bet)

            if money_start >= bet:
                money_start -= bet
                result = random.choices(slot_symbols, k=3)
                print(f"\n{BOLD}Крутимо барабан...{RESET} ")

                for n in result:
                    time.sleep(0.5)
                    print(n, end=" ", flush=True)
                print("\n")

                if all(i == result[0] for i in result):
                    win = symbols_dict.get(result[0], 5)
                    win_amount = win * bet
                    if result[0] == "7️⃣":
                        print(f"{YELLOW}{BOLD}🎉 ДЖЕКПОТ! Ви зірвали куш! Виграш: {win_amount} ₴{RESET}\n")
                    else:
                        print(f"{GREEN}✨ Блискуче! Лінія зійшлася! Виграш: {win_amount} ₴{RESET}\n")

                    money_start += win_amount

                elif len(set(result)) == 2:
                    print(f"{GREEN}👍 Непогано! Збіг двох символів. Виграш: {bet * 2} ₴{RESET}\n")
                    money_start += bet * 2

                else:
                    print(f"{RED}💨 Фортуна відвернулася. Ви втратили {bet} ₴.{RESET}\n")
                    if money_start <= 0:
                        print(f"{RED}{BOLD}Гроші закінчилися! До зустрічі!{RESET}")
                        break

            else:
                print(f"{RED}❌ Недостатньо коштів для такої ставки.{RESET}\n")

        else:
            print(f"{RED}❌ Помилка: Введіть коректну суму цифрами (більше нуля).{RESET}\n")

    elif choice == "2":
        print(f"{YELLOW}{BOLD}💰 Ви забираєте {money_start} ₴. Чудова гра! До зустрічі!{RESET}")
        break

    else:
        print(f"{RED}❌ Невідома команда. Спробуйте ще раз.{RESET}\n")




