import random
from operator import add, sub, mul
from brain_games import engine

WELCOME_TEXT = 'What is the result of the expression?'
INPUT_TYPE = 'real'


def generate_question():
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    a = engine.generate_random_number()
    b = engine.generate_random_number()
    op, operation = random.choice(list(operations.items()))

    return f'{a} {op} {b}', operation(a, b)
