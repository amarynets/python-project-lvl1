from brain_games import engine

WELCOME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
INPUT_TYPE = 'str'


def is_prime(number):
    if number < 2 or not number % 2:
        return False
    for i in range(3, number // 2, 2):
        if not number % i:
            return False
    return True


def generate_question():
    question = engine.generate_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
