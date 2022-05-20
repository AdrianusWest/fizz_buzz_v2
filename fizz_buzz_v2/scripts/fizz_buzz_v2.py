#!/usr/bin/env python3
import signal

import prompt

from fizz_buzz_v2.fizz_buzz_v2 import fizz_buzz, sigint_handler


def main():
    print('Welcome to Fizz Buzz!\n'
          'Submit a number and get an answer!!')
    while True:
        input_number = prompt.integer(prompt='Number: ')
        print(fizz_buzz(input_number))


signal.signal(signal.SIGINT, sigint_handler)


if __name__ == '__main__':
    main()
