import prompt

from brain_games.scripts.welcome_user import welcome_user

# Общая логика для всех игр:
# задать вопрос, получить ответ, сравнить ответ; везде 3 вопроса,
# реакции на верные и неверные ответы одинаковые


def question(mini_game, show_rules) -> None:  # общая логика всех мини-игр
    player_name: str = welcome_user()  # приветствие + узнаём имя игрока
    show_rules()  # объсняем правила идущей мини-игры
    streak: int = 0
    MAX_ATTEMPTS = 3
    while streak != MAX_ATTEMPTS:
        unknown: str
        correct_answer: str
        unknown, correct_answer = mini_game()
        print(f"Question: {unknown}")
        answer: str = prompt.string('Your answer: ')
        if answer == correct_answer:  # сравниваем ответ игрока с правильным
            print('Correct!')
            streak += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            return print(f"Let's try again, {player_name}!")
    return print(f"Congratulations, {player_name}!")
