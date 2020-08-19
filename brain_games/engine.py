import prompt


def start(game):
    print('Welcome to the Brain Games!')
    print(game.WELCOME_TEXT)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    num_of_correct_answer = 0
    for _ in range(3):
        question, answer = game.generate_question()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer != answer:
            msg = f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'."  # noqa: E501
            print(msg)
            break
        num_of_correct_answer += 1
        print('Correct!')
    if num_of_correct_answer == 3:
        print(f'Congratulations, {name}!')
