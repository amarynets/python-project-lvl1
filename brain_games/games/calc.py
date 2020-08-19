import random
from operator import sub, mul

WELCOME_TEXT = 'What is the result of the expression?'


def generate_question():
    operations = {
        '+': lambda x, y: x + y,
        '-': sub,
        '*': mul,
    }
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    op, operation = random.choice(list(operations.items()))

    return f'{a} {op} {b}', str(operation(a, b))
