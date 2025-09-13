from brain_games.scripts.welcome_user import welcome_user
import prompt

# Общая логика для всех игр:
# задать вопрос, получить ответ, сравнить ответ; везде 3 вопроса
# реакции на верные и неверные ответы одинаковые

def question(mini_game, rules):  # общая логика всех мини-игр
    player_name = welcome_user()  # приветствие + узнаёи имя игрока
    rules()  # объсняем правила идущей мини-игры
    cycles: int = 0  # отсчёт циклов с верными ответами
    while cycles != 3:
        # запускается функция для выбора неизвестного под конкретную игру 
        # и содержащая в себе правильный ответ
        unknown, correct_answer = mini_game()
        print(f"Question: {unknown}")  # задаём игроку вопрос с полученным выше неизвестным
        answer = prompt.string('Your answer: ')  # просим ввести ответ и получаем ввод
        if answer == correct_answer:  # сравниваем ответ игрока с правильным
            print('Correct!') # ответ верный
            cycles += 1
        else:  # ответ неверный
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {player_name}!")  # проигрыш, завершение игры
    return print(f"Congratulations, {player_name}!")  # выигрыш, завершение игры

