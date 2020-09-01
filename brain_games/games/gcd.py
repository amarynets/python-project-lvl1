import random
import math

WELCOME_TEXT = 'Find the greatest common divisor of given numbers.'
ANSWER_TYPE = 'int'


def generate_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    return f'{a} {b}', math.gcd(a, b)
