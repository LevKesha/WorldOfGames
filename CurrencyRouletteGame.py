from currency_converter import CurrencyConverter

c = CurrencyConverter()


def get_money_interval(difficulty, usd):
    delta = 5 - int(difficulty)
    nis = c.convert(int(usd), 'USD', 'ILS')
    return nis + delta, nis - delta


def get_guess_from_user(usd):
    user_guess = float(input("Hou much Shekels is " + str(usd) + "USD?"))
    return user_guess


def play(difficulty):
    usd = input("What is the total amount of USD you have? ")
    (usd_total) = get_money_interval(difficulty, usd)
    nis_guess = get_guess_from_user(usd)
    max_usd = usd_total[0]
    min_usd = usd_total[1]
    if max_usd >= nis_guess >= min_usd:
        return True
    else:
        return False


