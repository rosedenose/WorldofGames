import random

def generate_number():
    num = 0
    problem_num = 1
    while problem_num == 1:
        problem_num = 0
        num = random.choice(range(10000, 100000))
        check = len(set(list(str(num))))
        if len(list(str(num))) > check:
            problem_num = 1
    return num


def get_user_guess():
    error = 1
    guess = 0
    while error == 1:
        error = 0
        try:
            guess = int(input("\nPlease input a 5 digit number: "))
        except ValueError:
            error = 1
        except EOFError:
            error = 1
        if len(list(str(guess))) != 5:
            print("\nYou've put in a wrong number of digits.")
            error = 1
    return guess


def play(difficulty):
    print(f"In this game you need to guess a 5 unique digit number in {9-difficulty} tries")
    num = generate_number()
    num_list = list(str(num))
    hit_score = 0
    for test in range(9-difficulty):
        near_hit_score = 0
        guess = list(str(get_user_guess()))
        for x in range(5):
            if guess[x] == num_list[x]:
                hit_score = hit_score + 1
                continue
            elif guess[x] in num_list:
                near_hit_score = near_hit_score + 1
                continue
        print(f"You got {hit_score} hits and {near_hit_score} near hits \nyou've got {8 - difficulty - test} tries")
    if hit_score == 5:
        return True
    else:
        return False



