import os.path
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    scores_file = open(SCORES_FILE_NAME, 'a')
    scores_size = os.path.getsize("Scores.txt")
    points_of_winning = int(difficulty)*3 + 5
    if scores_size > 0:
        scores_file.write(', ' + str(points_of_winning))
    else:
        scores_file.write(str(points_of_winning))




