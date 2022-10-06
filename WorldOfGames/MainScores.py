from flask import Flask
import re
from utils import err_report
import threading
from selenium import webdriver


def read_score(name):
    your_score = 0
    scores = []
    file_read = 0
    try:
        scores = open("scores.txt")
        file_read = 1
    except:
        print("could not open the file")
        err_report()
    if file_read == 1:
        for line in scores.readlines():
            if name in str(line):
                your_score = re.sub(name, "", line)
            else:
                err_report()
        scores.close()
    return your_score


def present_score(player):
    err_log = open("err.txt")
    status = err_log.readlines()
    # print(status[0])
    app = Flask(__name__)
    print(__name__)
    SCORE = read_score(player)
    ERROR = 'There was an error somewhere along the way. '

    if str(status[0]) == "0":
        @app.route('/')
        def success():
            a = f"""<html>    
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                        <h1>The score is <div id="score">{SCORE}</div></h1>
                        </body>
                    </html>"""
            return a, 200
    elif str(status[0]) != "0":
        @app.route('/')
        def failure():
            b = f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1><div id="score" style="color:red">{ERROR}</div></h1>
                        </body>
                    </html>"""
            return b, 200
    if __name__ == "MainScores":
        first_thread = threading.Thread(target=app.run(host='0.0.0.0', port=4444))
        second_thread = threading.Thread(target=show_score())
        second_thread.start()
        first_thread.start()
    print("after flask")


def show_score():
    my_driver = webdriver.Chrome("chromedriver.exe")
    my_driver.get("http://127.0.0.1:4444")
# present_score("Alexey")
