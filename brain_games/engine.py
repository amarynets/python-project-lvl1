import random

import prompt

USER_INPUTS = {
    'str': prompt.string,
    'int': prompt.integer,
    'real': prompt.real
}

CORRECT_MSG = 'Correct!'
WRONG_MSG = "'{user_answer}' is wrong answer ;\
(. Correct answer was '{correct_answer}'."


def generate_random_number():
    return random.randint(0, 100)


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True, CORRECT_MSG
    msg = WRONG_MSG.format(
        user_answer=user_answer,
        correct_answer=correct_answer
    )
    return False, msg


def run_game(game):
    print('Welcome to the Brain Games!')
    print(game.WELCOME_TEXT)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    user_input_function = USER_INPUTS.get(game.INPUT_TYPE, prompt.string)

    engine(name, game.generate_question_answer_set, user_input_function)


def engine(user, game, user_input_function):
    correct_answer_counter = 0
    while correct_answer_counter < 3:
        question, correct_answer = game()
        user_answer = user_input_function(
            f'Question: {question}\nYour answer: '
        )
        status, msg = check_answer(user_answer, correct_answer)
        if not status:
            print(msg)
            return
        print(msg),
        correct_answer_counter += 1
    print(f'Congratulations, {user}!')
