import random


def generate_number(diff):
    secret_number = random.choice(range(diff+1))+1
    return secret_number

#print(generate_number(3))


def get_guess_from_user(diff):
    error = 1
    guess = 0
    while error == 1:
        error = 0
        try:
            guess = int(input(f"please guess a number from 1 to {diff+1}: "))
        except ValueError:
            error = 1
            print("You've entered a wrong value \n")
        except EOFError:
            error = 1
            print("You've entered a wrong value \n")
        if guess > (diff + 1) or guess < 1:
            error = 1
            print("You've entered a wrong value \n")
    return guess


def compare_results(secret, guess):
    if secret == guess:
        return 1
    elif secret != guess:
        return 0


def play(difficulty):
    secret = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    result = compare_results(secret, guess)
    if result == 1:
        return True
    elif result == 0:
        return False