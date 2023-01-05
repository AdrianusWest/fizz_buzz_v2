from fizz_buzz_v2.fizz_buzz_v2 import fizz_buzz


def test_fizz_buzz():
    assert fizz_buzz(11) == 11
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(6) == 'Fizz'
    assert fizz_buzz(15) == 'FizzBuzz'
