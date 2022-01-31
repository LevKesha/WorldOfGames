import random


def get_guess_from_user(difficulty):
    user_input = input("Please guess a number between 1 and " + str(difficulty))
    return user_input


def compare_results(user_input, secret_number):
    if user_input == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret = random.randint(0, int(difficulty))
    user = get_guess_from_user(difficulty)
    return compare_results(user, secret)
