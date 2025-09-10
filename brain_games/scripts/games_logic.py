from welcome_user import welcome_user

# Общая логика для всех игр:
# задать вопрос, получить ответ, сравнить ответ; везде 3 вопроса
# реакции на верные и неверные ответы одинаковые

def question():  # структура вопроса
    # number: int = randint(-100, 100)
    # first_question()/second_question()...
    print(f"Question: {number}")
    answer = prompt.string('Your answer: ')
    even = number % 2 == 0  # проверка на чётность
    return answer, even

def correct_answer_calc():
    # result from operation_signs() from brain_calc
 

def check_answer(answer, even):  # проверка ответа
    if even:  # -> True == заданное число чётное
        if answer == 'yes':  # проверка ввода пользователя 
            return True  # возврат булевого значения для функции main
        else:
            return False
    else:  # -> False == заданное число нечётное
        if answer == 'no':  # проверка ввода пользователя
            return True  # возврат булевого значения для функции main
        else:
            return False

def user_result(answer):
    player_name = welcome_user()
    if check_answer() is True:
        print('Correct!')
    else:  # нужно поправить, что идёт в correst answer, чтобы скрипт был универсальным
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        print(f"Let's try again, {player_name}!")
