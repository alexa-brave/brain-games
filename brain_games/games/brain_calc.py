from random import (
    choice,  # для случайного выбора оперантов
    randint,  # для случайного выбора чисел
)

from brain_games.scripts.games_logic import question


def rules_the_game() -> None:  # объясняем правила игры
    print('What is the result of the expression?')


# выбор неизвестных для одного раунда игры brain_calc
def is_calc_game() -> tuple[str, str]:
    num_1: int = randint(0, 100)  # генерируем первое число
    num_2: int = randint(0, 100)  # генерируем второе число
    # рандомизация выбора операнда
    operation_signs: str = choice(['+', '-', '*'])
    # выбираем действие и считаем результат
    unknown: str
    correct_answer: str
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


def main() -> None:
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_calc_game, rules_the_game)


if __name__ == "__main__":
    main()
