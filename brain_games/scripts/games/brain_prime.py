from random import randint

from brain_games.scripts.games_logic import question

# Игра «Простое ли число?»
# Функцию проверки является ли число простым,
# нужно реализовать самостоятельно, без библиотек


def rules_the_game() -> None:  # объясняем правила конкретной мини игры
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime_game() -> tuple[str, str]:
    # список простых чисел от 0 до 100
    SIMPLE_NUMS: list[int] = [2, 3, 5, 7, 11, 13, 17, 
                        19, 23, 29, 31, 37, 41, 
                        43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97]
    unknown: int = randint(0, 100)  # создаём неизвестное
    # проверяем, входит ли неизвестное в наш список
    # и сверяем ответ игрока с верным
    correct_answer: str
    if unknown in SIMPLE_NUMS:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(unknown), correct_answer


def main() -> None:  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_prime_game, rules_the_game)


if __name__ == "__main__":
    main()
