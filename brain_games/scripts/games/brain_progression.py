from random import randint

from brain_games.scripts.games_logic import question

# Показываем игроку ряд чисел, который образует арифметическую прогрессию,
# заменив любое из чисел двумя точками. Игрок должен определить это число.
# Рекомендуемая длина прогрессии – 10 чисел. Длина может генерироваться
# случайным образом, но должна содержать не менее пяти чисел. Позиция 
# спрятанного элемента каждый раз изменяется — 
# выбирается случайным образом


def rules_the_game():  # объясняем правила конкретной мини игры
    print('What number is missing in the progression?')


def is_progression_game():  # выбор неизвестных для одного раунда игры
    # задаём длину прогрессии в рамках рекомендуемой длины
    len_of_progression: int = randint(5, 15)
    start_num: int = randint(1, 100)  # задаём стартовое число
    step_of_progression: int = randint(1, 20)
    subsequence: list = [start_num]  # последовательность

    # выясняем оставшиеся числа прогрессии
    # цикл: длина прогрессии минус первоначально известный элемент
    for _ in range(len_of_progression - 1):
        # сумма последнего элемента прогрессии и длины шага прогрессии
        new_element: int = subsequence[-1] + step_of_progression
        # добавляем новый элемент в список прогрессии
        subsequence.append(new_element)
    
    # задаём позицию неизвестного числа
    position_unknown: int = randint(1, len_of_progression) - 1
    # правильный ответ для сравнения со вводом игрока
    correct_answer = subsequence[position_unknown]
    # удаляем неизвестное из списка прогрессии
    subsequence.remove(correct_answer)
    # ставим вместо неизвестного '..'
    subsequence.insert(position_unknown, '..')
    # последовательность с пропущеным неизвестным
    unknown: list = ' '.join(map(str, subsequence))
    return unknown, str(correct_answer)


def main():  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_progression_game, rules_the_game)


if __name__ == "__main__":
    main()
