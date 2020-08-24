import random
from operator import add, sub, mul

WELCOME_TEXT = 'What is the result of the expression?'


def generate_question():
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    op, operation = random.choice(list(operations.items()))

    return f'{a} {op} {b}', str(operation(a, b))
