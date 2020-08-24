import random

WELCOME_TEXT = 'Answer "yes" if number even otherwise answer "no".'
ANSWER_TYPE = 'str'


def generate_question():
    num = random.randint(0, 100)
    return num, 'yes' if num % 2 == 0 else 'no'
