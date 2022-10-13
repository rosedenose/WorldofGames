from flask import Flask
import re
from utils import err_report
import sys


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
            #else:
                #err_report()
        scores.close()
    return your_score


def present_score(player):
    err_log = open("err.txt")
    status = err_log.readlines()
    print(status[0])
    app = Flask(__name__)
    SCORE = read_score(player)
    ERROR = 'There was an error somewhere along the way. '

    if "0" in str(status):
        @app.route('/')
        def success():
            good = f"""<html>    
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>The score is <div id="score">{SCORE}</div></h1>
                        </body>
                    </html>"""
            return good, 200
    else:
        @app.route('/')
        def failure():
            bad = f"""<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1><div id="score" style="color:red">{ERROR}</div></h1>
                        </body>
                    </html>"""
            return bad, 200
    app.run(host='0.0.0.0', port=4444)

try:
    if sys.argv[1] == "1":
        present_score("test")
except:
    print("###############################################")