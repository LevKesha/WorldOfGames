from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    scores_file = open(SCORES_FILE_NAME, 'a')
    if scores_file:
        scores_file.write(', ' + str(difficulty))
    else:
        scores_file.write(str(difficulty))




