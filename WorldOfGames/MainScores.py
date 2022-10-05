from flask import Flask
import re
from utils import err_report


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
                print("can't find your name in the file")
                err_report()
        scores.close()
    return your_score

def present_score(player,status):
    err_log = open("err.txt")
    status = err_log.readlines()
    app = Flask(__name__)
    SCORE = read_score(player)
    ERROR = 'There was an error somewhere along the way. '
    if status == 0:
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
    elif status != 0:
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
    app.run(host='0.0.0.0', debug=True, port=5000)


#present_score("Alexey")