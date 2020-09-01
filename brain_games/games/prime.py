import random

WELCOME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_TYPE = 'str'


def is_prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if number % 2 == 0:
                return False
            elif number % 3 == 0:
                return False
            elif number % 5 == 0:
                return False
        return True
    return False


def generate_question():
    num = random.randint(1, 20)
    return num, 'yes' if is_prime(num) else 'no'
