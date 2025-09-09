import prompt

def welcome_user():  # приветствие игрока
    print('Welcome to the Brain Games!')
    # узнаём имя и обращаемся по нему
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name