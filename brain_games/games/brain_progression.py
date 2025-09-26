from random import randint

from brain_games.scripts.games_logic import question

# Арифметическая прогрессия с одним пропуском,
# который игроку нужно заполнить


def rules_the_game() -> None:
    print('What number is missing in the progression?')


def is_progression_game() -> tuple[str, str]:
    len_of_progression: int = randint(5, 15)
    start_num: int = randint(1, 100)
    step_of_progression: int = randint(1, 20)
    subsequence: list = [start_num]  # последовательность

    START_LEN_PROGRESSION: int = 1
    for _ in range(len_of_progression - START_LEN_PROGRESSION):
        new_element: int = subsequence[-1] + step_of_progression
        subsequence.append(new_element)
    
    position_unknown: int = (
    randint(1, len_of_progression) - START_LEN_PROGRESSION
    )
    correct_answer: int = subsequence[position_unknown]
    # удаляем неизвестное из списка прогрессии
    subsequence.remove(correct_answer)
    # ставим вместо неизвестного '..'
    subsequence.insert(position_unknown, '..')
    # последовательность с пропущеным неизвестным
    unknown: str = ' '.join(map(str, subsequence))
    return unknown, str(correct_answer)


def main() -> None:
    question(is_progression_game, rules_the_game)


if __name__ == "__main__":
    main()
