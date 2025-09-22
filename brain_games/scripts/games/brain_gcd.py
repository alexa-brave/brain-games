from random import randint  # для случайного выбора чисел
import math
import sys
from brain_games.scripts.games_logic import question

# пользователю показывается два случайных числа, например,
# 25 50. Пользователь должен вычислить и ввести наибольший
# общий делитель этих чисел.

# Реализуйте необходимую логику для работы игры
# Проверьте работоспособность новой игры
# Добавьте в README.md аскинему с запуском и демонстрацией различных исходов игры

def rules_the_game():  # объясняем правила игры
    print('Find the greatest common divisor of given numbers.')

def unknows():  # поиск неизвестных
    # рандомизация неизвестных мини-игры
    num_1: int = randint(-100, 100)
    num_2 = 0
    # проверка, чтобы оба числа не были нулями одновременно
    if num_1 == 0:
        while num_2 == 0:
            num_2: int = randint(-100, 100)
    else:
        num_2: int = randint(-100, 100)
        print(num_1, num_2)
    return num_1, num_2

def correct_answer():
    num_1, num_2 = unknows()  # разбиваем кортеж на переменные
    correct_answer = math.gcd(num_1, num_2)  # выясняем правильный ответ
    return correct_answer

def brain_gcd():
    a = unknows()
    b = correct_answer()
    print(a, b)


def main():  # точка входа для мини-игры brain-gcd
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(brain_gcd, rules_the_game)

if __name__ == '__main__':
    main()
