def welcome(name):
    return f"Hello {name} and welcome to World of Games (WoG). \nHere you can find many cool games to play.\n"


def user_int_input(string):
    error = 1
    input_int = 0
    while error == 1:
        error = 0
        try:
            input_int = int(input(f"\n{string}"))
        except ValueError:
            error = 1
        except EOFError:
            error = 1
    return input_int


def load_game():
    menu = open("menu.txt")
    for line in menu.readlines():
        print(line, end='')
    menu.close()
    game = 0
    difficulty = 0
    game_error = 1
    dif_error = 1
    while game_error == 1:
        user_int_input("Please choose game from 1 - 3, your choice:  ")
        if len(str(game)) != 1 or 4 < game or game < 1 or game_error == 1:
            print("\nyou have chosen an incorrect game option please try again.")
            game_error = 1
    while dif_error == 1:
        user_int_input("Please choose game difficulty from 1 to 5: ")
        if len(str(difficulty)) != 1 or 5 < difficulty or difficulty < 1 or dif_error == 1:
            print("\nyou have chosen an incorrect difficulty option please try again.")
            dif_error = 1
    return game, difficulty


load_game()