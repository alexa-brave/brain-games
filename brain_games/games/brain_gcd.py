import math
from random import randint  # для случайного выбора чисел

from brain_games.scripts.games_logic import question

# Вычисление НОД для двух рандомных чисел


def rules_the_game() -> None:
    print('Find the greatest common divisor of given numbers.')


def is_gcd_game() -> tuple[str, str]:
    num_1: int = randint(-100, 100)
    num_2: int = 0
    # проверка, чтобы оба числа не были нулями одновременно
    if num_1 == 0:
        while num_2 == 0:
            num_2: int = randint(-100, 100)
    else:
        num_2: int = randint(-100, 100)
    # выясняем правильный ответ, используя функцию для поиска НОД
    # правильны ответ - строка для сравнения со вводом игрока
    correct_answer: str = str(math.gcd(num_1, num_2))
    # результат - строка для стандартизации аргументов в функции
    # логики вопросов, чтобы 2 числа были 1 аргументом
    unknown: str = f'{num_1} {num_2}'
    return unknown, correct_answer


def main() -> None:
    question(is_gcd_game, rules_the_game)


if __name__ == '__main__':
    main()
