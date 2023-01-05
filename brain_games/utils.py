import prompt


LVL_NUMBERS = 3


def run(module):

    print('Welcome to the Brain Games!')
    module.welcome()

    name = prompt.string('May I have your name?: ')
    print('Hello, {}!'.format(name))

    incorrect_text = 'is wrong answer. Correct answer was'

    for lvl_counter in range(LVL_NUMBERS):
        que_and_right = module.question_and_answer()
        (question, right) = que_and_right

        print(question)
        guess = prompt.string('Your answer: ')

        if guess == right:
            print('Correct!')
        else:
            print('{} {} {}.'.format(guess, incorrect_text, right))
            print("Let's try again, {}.".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))

