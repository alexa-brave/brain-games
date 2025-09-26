from random import randint

from brain_games.scripts.games_logic import question


def rules_the_game() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


# выбор неизвестных для одного раунда игры brain_even
def is_even_game() -> tuple[str, str]:
    unknown: int = (randint(0, 100))
    correct_answer: str = 'yes' if unknown % 2 == 0 else 'no'
    return str(unknown), correct_answer


def main() -> None:
    question(is_even_game, rules_the_game)


if __name__ == "__main__":
    main()
