from random import randint  # для случайного выбора чисел
from random import choice  # для случайного выбора оперантов
from brain_games.scripts.games_logic import question

# Калькулятор; делаем только +, - и *
# Операции, как и числа, выбираются случайным образом (другой блок random)

# Общая логика для всех игр:
# задать вопрос, получить ответ, сравнить ответ; везде 3 вопроса
# реакции на верные и неверные ответы одинаковые

# Задачи:
# написать код для этой игры в вакууме, подумать, как объединить
# логику игр в один отдельный файл, сделать файл точку входа
# main.py в scripts, аскинема в README.md

# функция объяснения игроку правил мини-игры

# calc == 2 рандомных числа и рандомный операнд, истинный ответ, тексты развилки ответа

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

# tasks:
# встроить правила игры после приветствия

def main():
    # объясняем правила игры
    print('What is the result of the expression?')
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(calc_game)





# def choice_numbers():
#     num_1: int = randint(-100, 100)
#     num_2: int = randint(-100, 100)
#     return num_1, num_2


# def operation_signs(num_1, num_2):  # выбор операнда и вычисление

#     signs: list = ['+', '-', '*'] # используемые операнды
#     play_signs = choice(signs)  # рандомизация выбора операнда
#     if play_signs == signs[0]:  # сопоставляем выбранный операнд с тем, какому индексу в списке он соответствует
#         result = num_1 + num_2  # производим соответствующую операцию с числами
#     elif play_signs == signs[1]:
#         result = num_1 - num_2
#     else:
#         result = num_1 * num_2
#     return result

if __name__ == "__main__":
    main()
