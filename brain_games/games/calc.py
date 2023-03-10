import random
from operator import add, sub, mul


SYMBOL, OPERATION = random.choice((
    ('+', add),
    ('-', sub),
    ('*', mul),
))


def welcome():
    print('What is the result of the expression?\n')


def question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = OPERATION(num1, num2)
    question = 'Question: {} {} {}'.format(num1, SYMBOL, num2)
    result = (question, str(answer))
    return result
