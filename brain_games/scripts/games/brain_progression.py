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

def is_progression_game():  # выбор неизвестных для одного раунда игры
    return unknown, correct_answer


def main():  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_progression_game, rules_the_game)

if __name__ == "__main__":
    main()
