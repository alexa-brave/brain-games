import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    player_name: str = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    return player_name