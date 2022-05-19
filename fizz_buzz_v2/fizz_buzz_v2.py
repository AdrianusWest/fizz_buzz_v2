import prompt
import signal
import sys


def fizz_buzz(input_number):
    if input_number % 15 == 0:
        return 'FizzBuzz'
    elif int(input_number) % 3 == 0:
        return 'Fizz'
    elif int(input_number) % 5 == 0:
        return 'Buzz'
    else:
        return input_number


def sigint_handler(signal, frame):
    print('\nThe program is completed')
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


def main():
    print('Welcome to Fizz Buzz!\n'
          'Submit a number and get an answer!!')
    while True:
        input_number = prompt.integer(prompt='Number: ')
        print(fizz_buzz(int(input_number)))


if __name__ == '__main__':
    main()
