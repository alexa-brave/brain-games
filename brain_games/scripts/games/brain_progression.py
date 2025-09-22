from random import randint
from random import choice
from brain_games.scripts.games_logic import question
# Показываем игроку ряд чисел, который образует арифметическую прогрессию,
# заменив любое из чисел двумя точками. Игрок должен определить это число.

# Рекомендуемая длина прогрессии – 10 чисел. Длина может генерироваться случайным образом, 
# но должна содержать не менее пяти чисел
# Позиция спрятанного элемента каждый раз изменяется — 
# выбирается случайным образом

def rules_the_game():  # объясняем правила конкретной мини игры
    print('What number is missing in the progression?')

# ошибка в цикле, list.remove(x): x not in list

def is_progression_game():  # выбор неизвестных для одного раунда игры
    len_of_progression: int = randint(5, 15)
    start_num: int = randint(1, 100)
    step_of_progression: int = randint(1, 9)
    position_unknown: int = randint(1, len_of_progression) - 1
    # последовательность
    subsequence: list = [start_num]
    for i in list(range(len_of_progression + 1)):
        new_element: int = subsequence[-1] + step_of_progression
        subsequence.append(new_element)
        # remove(x)
        # pop([i])
    correct_answer = subsequence[position_unknown]
    subsequence.remove(position_unknown)
    unknown: list = subsequence.insert(position_unknown - 1, '..')
    print(subsequence)
    return unknown, correct_answer


def main():  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_progression_game, rules_the_game)

if __name__ == "__main__":
    main()
