# from os import name  -> пока не используем
from random import randint
from brain_games.scripts.games_logic import question

# Пользователю показывается случайное
# число. И ему нужно ответить yes,если
# число чётное, или no — если нечётное.

# even == 1 рандомное число, истинный ответ, тексты развилки ответа

def is_even_game():  # выбор неизвестных для одного раунда игры brain_even
    # рандомизация неизвестного мини-игры
    unknown: int = (randint(0, 100))
    # выяснение верного ответа
    correct_answer = 'yes' if unknown % 2 == 0 else 'no'
    # наружу выдаём неизвестное и правильный ответ
    return unknown, correct_answer


def main():  # точка входа для мини-игры brain-even
    # объясняем правила игры
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_even_game)


if __name__ == "__main__":
    main()
