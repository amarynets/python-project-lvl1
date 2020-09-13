from brain_games import engine

WELCOME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
INPUT_TYPE = 'str'


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
    question = engine.generate_random_number()
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
