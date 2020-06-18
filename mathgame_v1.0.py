import random
import operator
import time

delay = 0.5
rounds = 10

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print (f'what is:', num_1, operation, num_2,'?\n')
    return answer


def ask_question():
    answer = random_problem()
    guess = float(input())
    print('\n\n')
    return guess == answer


def game():
    print('\n\nMathgame\n+By: Even')
    print(''*4)
    score = 0
    for times in range(rounds):
        print('round:', score+1,)
        print('>'*8, '\n')
        if ask_question() == True:
            score += 1
            print('\u001b[32mCorrect!\n\n')
            #time.sleep(delay)
        else:
            print('\u001b[31mIncorrect\n')
            print(times)
            #time.sleep(delay)
    print('#'*16)
    print (f'your score is:\n', score, '/', times+1)
    print('#'*16)
game()
