from brain_games import engine


WELCOME_TEXT = 'Answer "yes" if number even otherwise answer "no".'
INPUT_TYPE = 'str'


def generate_question_answer_set():
    question = engine.generate_random_number()
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
