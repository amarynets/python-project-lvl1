import math
from brain_games import engine


WELCOME_TEXT = 'Find the greatest common divisor of given numbers.'
INPUT_TYPE = 'int'


def generate_question():
    a = engine.generate_random_number()
    b = engine.generate_random_number()
    question = f'{a} {b}'
    answer = math.gcd(a, b)
    return question, answer
