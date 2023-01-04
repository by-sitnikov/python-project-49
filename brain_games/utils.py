import prompt
import random

def start_game():
    count = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while True:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')

        if random_number % 2 == 0 and answer == 'yes' or random_number % 2 != 0 and answer == 'no':
            count += 1
            print('Currect!')
        else:
            if random_number % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break

        if count == 3:
            print(f'Congratulations, {name}!')
            break

