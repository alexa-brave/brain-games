from random import randint  # для случайного выбора чисел
from brain_games.scripts.games_logic import question

# пользователю показывается два случайных числа, например,
# 25 50. Пользователь должен вычислить и ввести наибольший
# общий делитель этих чисел.

# Реализуйте необходимую логику для работы игры
# Добавьте еще одну запись в секцию [project.scripts] в pyproject.toml
# Проверьте работоспособность новой игры
# Добавьте в README.md аскинему с запуском и демонстрацией различных исходов игры


# to do:
# сделать логику мини игры такой, чтобы цепочки функций не ломались
# прописать комментарии к своему коду
# короткая команда
# аскинема
# 

def rules_the_game():  # объясняем правила игры
    print('Find the greatest common divisor of given numbers.')

def unknows_the_game():  # поиск неизвестных
    # рандомизация неизвестных мини-игры
    num_1 = randint(-100, 100)  # unknow_1
    dividend = False  # делится ли делимое на делитель
    while not dividend:
        num_2 = randint(-100, 100)
        if num_1 != num_2:  # проверка, чтобы числа не были одинаковыми
            if num_1 % num_2 == 0 or num_2 % num_1 == 0:
                dividend = True
    return print(num_1, num_2)

def gcd1_game(num_1):  # ищем простые делители 1 числа
    # список простых чисел до 100
    past_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    i = 0
    dividend_1_list = []
    while past_nums[i] <= num_1:
        if num_1 % past_nums[i] == 0:
            dividend_1_list.append(past_nums[i])
            i += 1
    return dividend_1_list

def gcd2_game(num_2): # ищем простые делители 2 числа, сравниваем с вычитанием и ищем наибольший делитель, то есть, правильный ответ
    past_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    i = 0
    dividend_2_list = []
    while past_nums[i] <= num_2:
        if num_2 % past_nums[i] == 0:
            dividend_2_list.append(past_nums[i])
            i += 1
    return dividend_2_list

def gcd_ready(dividend_1_list, dividend_2_list):
    common_elements = dividend_1_list & dividend_2_list
    max_dividend = max(common_elements)
    print(common_elements)
    correct_answer = max_dividend
    return correct_answer

def main():  # точка входа для мини-игры brain-gcd
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(gcd_game, rules_the_game)

if __name__ == '__main__':
    main()
