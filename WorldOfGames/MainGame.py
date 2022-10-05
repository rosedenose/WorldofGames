import os
import GuessGame
import MemoryGame
import CurrencyRullette
import SecretGame
import Live
import Score
import MainScores
from selenium import webdriver

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
    score = Score.add_score(difficulty, name)
    print (score)
    #MainScores.present_score(name)
    #my_driver = webdriver.chrome(excutable_path="C:/Users/lysen/Downloads/chromedriver_win32/chromedriver.exe")
    #my_driver.get("http://127.0.0.1:5000/success")
elif res == False:
    print("uh, you lost. Try again next time")

# Show scoring

