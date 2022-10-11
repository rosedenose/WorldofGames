import GuessGame
import MemoryGame
import CurrencyRullette
import SecretGame
import Live
import Score
import MainScores
from selenium import webdriver


err = open("err.txt", "w")
err.write("0")
err.close()
name = str(input("Hello please enter your name: "))
print(Live.welcome(name))
game, difficulty = Live.load_game()
res = False

if game == 1:
    res = GuessGame.play(difficulty)
elif game == 2:
    res = MemoryGame.play(difficulty)
elif game == 3:
    res = CurrencyRullette.play(difficulty)
elif game == 4:
    res = SecretGame.play(difficulty)

# Scoring
if res == True:
    print("Hooray, you've won!!!")
    Score.add_score(difficulty, name)
    MainScores.present_score(name)
elif res == False:
    print("uh, you lost. Try again next time")
    MainScores.present_score(name)

# Show scoring
