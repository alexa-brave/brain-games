from os import name
import prompt

# Пользователю показывается случайное
# число. И ему нужно ответить yes,если
# число чётное, или no — если нечётное.

def welcome_user():  # приветствие игрока
    print('Welcome to the Brain Games!')
    # узнаём имя и обращаемся по нему
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    # объясняем игроку суть игры
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    welcome_user()
    if first_question() == 'Correct!':
        if second_question() == 'Correct!':
            if third_question() == 'Correct!':
                print(f"Congratulations, {name}!")
    

def first_question():
    print('Question: 15')
    ancwer = prompt.string('Your answer: ')
    if ancwer == 'no':
        print('Correct!')
    else:
        print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, {name}!")

def second_question():
    print('Question: 6')
    ancwer = prompt.string('Your answer: ')
    if ancwer == 'yes':
        print('Correct!')
    else:
        print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again, {name}!")

def third_question():
    print('Question: 7')
    ancwer = prompt.string('Your answer: ')
    if ancwer == 'no':
        print('Correct!')
    else:
        print(f"'{ancwer}' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, {name}!")

if __name__ == "__main__":
    main()
