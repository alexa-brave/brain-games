from brain_games.scripts.games_logic import question


# Игра «Простое ли число?»

def rules_the_game():  # объясняем правила конкретной мини игры
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

def is_prime_game():
    # main_skript

def main():  # точка входа для мини-игры
    # запускаем универсальную для всех мини-игр функцию
    # даём ей на вход неизвестное и правильный ответ для этой мини-игры
    question(is_prime_game, rules_the_game)

if __name__ == "__main__":
    main()
