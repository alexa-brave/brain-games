from brain_games.scripts.welcome_user import welcome_user
import prompt

# Общая логика для всех игр:
# задать вопрос, получить ответ, сравнить ответ; везде 3 вопроса
# реакции на верные и неверные ответы одинаковые

def question(unknown, correct_answer):  # общая логика всех мини-игр
    print(f"Question: {unknown}")
    cycles: int = 0  # отсчёт циклов с верными ответами
    while cycles != 3:
        answer = prompt.string('Your answer: ')  # просим ввести ответ и получаем ввод
        if answer == correct_answer:  # сравниваем ответ игрока с правильным
            print('Correct!') # ответ верный
            cycles += 1
        else:  # ответ неверный
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {player_name}!")  # проигрыш, завершение игры
        return print(f"Congratulations, {player_name}!")  # выигрыш
        
