import random
import prompt


def run():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    questions = [random.randint(0, 100) for _ in range(3)]
    num_of_correct_answers = 0
    for question in questions:
        answer = 'yes' if question % 2 == 0 else 'no'
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer.lower() != answer:
            msg = f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'."  # noqa: E501
            print(msg)
            break
        num_of_correct_answers += 1
        print('Correct!')
    if num_of_correct_answers == len(questions):
        print(f'Congratulations, {name}!')
