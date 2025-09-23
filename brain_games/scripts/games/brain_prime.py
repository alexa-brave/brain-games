from brain_games.scripts.games_logic import question
from random import randint

# Игра «Простое ли число?»

# Функцию проверки является ли число простым, нужно реализовать самостоятельно, без библиотек

# To do:
# Добавьте в README.md аскинему с запуском и демонстрацией различных исходов игры

def rules_the_game():  # объясняем правила конкретной мини игры
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

def is_prime_game():
    simple_nums: list = [2, 3, 5, 7, 11, 13, 17, 
                        19, 23, 29, 31, 37, 41, 
                        43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97]
    unknown: int = randint(0, 100)
    if unknown in simple_nums:
        correct_answer: str = 'yes'
    else:
        correct_answer = 'no'
    return unknown, correct_answer

def main():  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_prime_game, rules_the_game)

if __name__ == "__main__":
    main()
