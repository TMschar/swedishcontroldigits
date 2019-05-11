#!/usr/env/bin python3

import math


def add_control_digit(original_digits: str, add_length: bool=True):
    if len(original_digits) >= 23:
        raise(Exception('Cannot be longer than 23'))

    original_digits = str(original_digits)

    length_str = ''
    all_digits = []
    multiply_by = 2
    control_digit = 0

    if add_length:
        length_str = str(len(original_digits) + 2)

    if len(length_str) > 1:
        length_str = length_str[1]

    digits = original_digits + length_str
    rev_digits = digits[::-1]

    for digit in rev_digits:
        multiplied = str(int(digit) * multiply_by)

        for multiplied_digit in multiplied:
            all_digits.append(int(multiplied_digit))

        if multiply_by == 2:
            multiply_by = 1
        else:
            multiply_by = 2

    for digit in all_digits:
        control_digit += digit

    next_ten = math.ceil(control_digit / 10) * 10
    control_digit = next_ten - control_digit

    if control_digit == 10:
        control_digit = 0

    return f'{original_digits}{length_str}{control_digit}'


if __name__ == '__main__':
    add_length = bool(input("Add length (True/False): "))
    check = str(input("Digits to create check for: "))
    output = add_control_digit(check, add_length)

    print(f'\nResult: {output}')
