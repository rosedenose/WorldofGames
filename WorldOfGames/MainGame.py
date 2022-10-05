import os
import GuessGame
import MemoryGame
import CurrencyRullette
import SecretGame
import Live
import Score

name = str(input("Hello please enter your name: "))
print(Live.welcome(name))
game, difficulty = Live.load_game()

if game == 1:
    res = GuessGame.play(difficulty)
    if res == True:
        print("Hooray, you've won!!!")
        Score.add_score(difficulty, name)
    elif res == False:
        print("uh, you lost. Try again next time")
elif game == 2:
    res = MemoryGame.play(difficulty)
    if res == True:
        print("Hooray, you've won!!!")
        Score.add_score(difficulty, name)
    elif res == False:
        print("uh, you lost. Try again next time")
elif game == 3:
    res = CurrencyRullette.play(difficulty)
    if res == True:
        print("Hooray, you've won!!!")
        Score.add_score(difficulty, name)
    elif res == False:
        print("uh, you lost. Try again next time")
elif game == 4:
    res = SecretGame.play(difficulty)
    if res == True:
        print("Hooray, you've won!!!")
        Score.add_score(difficulty, name)
    elif res == False:
        print("uh, you lost. Try again next time")