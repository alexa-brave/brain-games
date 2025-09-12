from os import name
import prompt
from random import randint
from ..welcome_user import welcome_user

# Пользователю показывается случайное
# число. И ему нужно ответить yes,если
# число чётное, или no — если нечётное.

def start():  # объясняем правила игры
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():  # функция - точка входа для brain_even
    player_name = welcome_user()
    if first_question() is True:
        print('Correct!')
        if second_question() is True:
            print('Correct!')
            if third_question() is True:
                print('Correct!')
                print(f"Congratulations, {player_name}!")
            else:
                print(f"Let's try again, {player_name}!")
        else:
            print(f"Let's try again, {player_name}!")
    else:
        print(f"Let's try again, {player_name}!")
    

def first_question():  # первый вопрос
    first_number: int = randint(-100, 100)
    print(f"Question: {first_number}")
    ancwer = prompt.string('Your answer: ')
    even = first_number % 2 == 0  # проверка на чётность
    if even:
        if ancwer == 'yes':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'yes'.")
            # print(f"Let's try again, {player_name}!")
            return False
    else:
        if ancwer == 'no':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'no'.")
            # print(f"Let's try again, {player_name}!")
            return False


def second_question():  # второй вопрос
    second_number: int = randint(-100, 100)
    print(f"Question: {second_number}")
    ancwer = prompt.string('Your answer: ')
    even = second_number % 2 == 0  # проверка на чётность
    if even:
        if ancwer == 'yes':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'yes'.")
            # print(f"Let's try again, {player_name}!")
            return False
    else:
        if ancwer == 'no':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'no'.")
            # print(f"Let's try again, {player_name}!")
            return False

def third_question():   # третий вопрос
    third_number: int = randint(-100, 100)
    print(f"Question: {third_number}")
    ancwer = prompt.string('Your answer: ')
    even = third_number % 2 == 0  # проверка на чётность
    if even:
        if ancwer == 'yes':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'yes'.")
            # print(f"Let's try again, {player_name}!")
            return False
    else:
        if ancwer == 'no':  # проверка ввода пользователя
            # print('Correct!')
            return True  # возврат булевого значения для функции main
        else:
            print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'no'.")
            # print(f"Let's try again, {player_name}!")
            return False

if __name__ == "__main__":
    main()


# even == 1 рандомное число, истинный ответ, тексты развилки ответа
# calc == 2 рандомных числа и рандомный операнд, истинный ответ, тексты развилки ответа

def is_even_game():  # выбор неизвестных для одного раунда игры brain_even
    unknown: int = (randint(0, 100))
    correct_answer = 'yes' if unknown % 2 == 0 else 'no'
    return unknown, correct_answer