from flask import Flask, render_template
from Utils import SCORES_FILE_NAME


def score_server():
    app = Flask(__name__)

    def send_score():
        res = 0
        score_file = open(SCORES_FILE_NAME, 'r').readlines()
        if score_file is None:
            return render_template("ScoresError.html", ERROR="Can't open file"), 400
        while score_file:
            res = res + int(score_file.pop())
        return render_template("ScoresSuccess.html", SCORE=res), 200

    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True, port=8080)





