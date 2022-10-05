import requests
import json
import ast
import random


def get_money_interval(difficulty):
    interval = 6 - difficulty
    return interval


def get_guess_from_user():
    guess = 0
    error = 1
    while error == 1:
        error = 0
        try:
            guess = int(input("please enter your guess: "))
        except ValueError:
            error = 1
            print("You've entered a wrong value \n")
        except EOFError:
            error = 1
            print("You've entered a wrong value \n")
    return guess


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def play(difficulty):
    interval = get_money_interval(difficulty)
    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd.json'
    response = requests.get(url)
    if str(response) != "<Response [200]>":
        print("there is an issue with internet connection please try again later\n")
    lines = ast.literal_eval(jprint(response.json()))
    dollar = lines['usd']
    conversion = dollar['ils']
    in_dollar = random.choice(range(100))
    print(f"the sum is {in_dollar}$\n")
    guess = get_guess_from_user()
    in_shekel = in_dollar * conversion
    if (in_shekel - interval) < guess < (in_shekel + interval):
        return True
    else:
        return False
