import sys


def fizz_buzz(input_number):
    if input_number % 15 == 0:
        return 'FizzBuzz'
    elif input_number % 3 == 0:
        return 'Fizz'
    elif input_number % 5 == 0:
        return 'Buzz'
    else:
        return input_number


def sigint_handler(signal, frame):
    print('\nThe program is completed')
    sys.exit(0)
