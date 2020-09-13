import random
from brain_games import engine

WELCOME_TEXT = 'What number is missing in the progression?'
INPUT_TYPE = 'int'


def generate_question():
    start = engine.generate_random_number()
    step = random.randint(1, 10)
    missed_item_index = random.randint(0, 9)
    progression = list(range(start, start + step * 10, step))
    answer = progression[missed_item_index]
    progression[missed_item_index] = '..'
    return str(progression), answer
