from flask import Flask
import re


def read_score(name):
    your_score = 0
    scores = []
    file_read = 0
    status = 0
    try:
        scores = open("scores.txt")
        file_read = 1
    except:
        print("could not open the file")
    if file_read == 1:
        for line in scores.readlines():
            if name in str(line):
                your_score = re.sub(name, "", line)
                status = 1
            else:
                print("can't find your name in the file")
        scores.close()
    return your_score, status

def present_score(player):
    app = Flask(__name__)
    result = read_score(player)
    SCORE = result[0]
    status = result[1]
    ERROR = 'There was an error somewhere along the way. '
    if status == 1:
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
    elif status != 1:
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