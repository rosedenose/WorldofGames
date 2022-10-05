import os
from time import sleep
import random
import ast


def generate_sequence(difficulty):
    numbers = []
    for num in range(difficulty):
        random_number = random.choice(range(101))
        while random_number in numbers:
            random_number = random.choice(range(101))
        numbers.append(random_number)
    print(numbers)
    sleep(0.7)
    os.system('cls')
    return numbers


def get_list_from_user(difficulty):
    guess = []
    error = 1
    while error == 1:
        error = 0
        try:
            guess = ast.literal_eval(input("please enter your guess (numbers separated by commas): "))
        except ValueError:
            print("the value entered is wrong\n")
            error = 1
            continue
        except EOFError:
            print("the value entered is wrong\n")
            error = 1
            continue
        except SyntaxError:
            print("the value entered is wrong\n")
            error = 1
            continue
        if type(guess) == int:
            continue
        else:
            for num1 in guess:
                if guess.count(num1) > 1:
                    error = 1
                    print("all the numbers are unique you cannot guess the same number more than once\n")
                    break
            if len(guess) > difficulty:
                print("you've put in too many guesses\n")
                error = 1
            elif len(guess) < difficulty:
                print("You've put to few guesses\n")
                error = 1
    return guess

def is_list_equal(numbers, guess_list):
    score = 0
    if type(guess_list) == int:
        if guess_list in numbers:
            score = 1
        if score == 1:
            return True
        else:
            return False
    else:
        for num in numbers:
            if num in guess_list:
                score = score + 1
        if score == len(guess_list):
            return True
        else:
            return False


def play(difficulty):
    generated_numbers = generate_sequence(difficulty)
    guessed_numbers = get_list_from_user(difficulty)
    result = is_list_equal(generated_numbers, guessed_numbers)
    return result