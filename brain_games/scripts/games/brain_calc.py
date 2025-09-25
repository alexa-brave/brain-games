from random import (
    choice,  # для случайного выбора оперантов
    randint,  # для случайного выбора чисел
)

from brain_games.scripts.games_logic import question


def rules_the_game():  # объясняем правила игры
    print('What is the result of the expression?')


def calc_game():  # выбор неизвестных для одного раунда игры brain_calc
    num_1, num_2 = (randint(0, 100), randint(0, 100))
    operation_signs = choice(['+', '-', '*'])  # рандомизация выбора операнда
    # выбираем действие и считаем результат
    match operation_signs:
        case '+':
            unknown = f"{num_1} + {num_2}"
            correct_answer = str(num_1 + num_2)
        case '-':
            unknown = f"{num_1} - {num_2}"
            correct_answer = str(num_1 - num_2)
        case '*':
            unknown = f"{num_1} * {num_2}"
            correct_answer = str(num_1 * num_2)
    return unknown, correct_answer


def main():
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(calc_game, rules_the_game)


if __name__ == "__main__":
    main()
