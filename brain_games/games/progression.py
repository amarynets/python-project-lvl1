import random

WELCOME_TEXT = 'What number is missing in the progression?'
ANSWER_TYPE = 'int'


def generate_question():
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    missed_item_index = random.randint(0, 9)
    progression = list(range(start, start + step * 10, step))
    answer = progression[missed_item_index]
    progression[missed_item_index] = '..'
    return str(progression), answer
