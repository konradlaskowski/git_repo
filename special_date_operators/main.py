from datetime import date, timedelta

date = date.today() - timedelta(days=1)

print(date)

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

while True:

    numb = input('Podaj liczbe: ')
    iss = is_digit(numb)
    print(iss)