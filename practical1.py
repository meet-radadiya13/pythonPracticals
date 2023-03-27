"""
    Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.
"""
number = ""
digits = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
output = ""


def word_to_num(string):
    """
    Converts a word representing a number to its numerical value.

    Args:
    string (str): A string representing a number in word form.

    Returns:
    str: The numerical value of the input string as a string.

    Raises:
    IndexError
    """
    if string.startswith('zero'):
        return number + '0' + word_to_num((string[4:]))
    elif string.startswith('one'):
        return number + '1' + word_to_num((string[3:]))
    elif string.startswith('two'):
        return number + '2' + word_to_num((string[3:]))
    elif string.startswith('three'):
        return number + '3' + word_to_num((string[5:]))
    elif string.startswith('four'):
        return number + '4' + word_to_num((string[4:]))
    elif string.startswith('five'):
        return number + '5' + word_to_num((string[4:]))
    elif string.startswith('six'):
        return number + '6' + word_to_num((string[3:]))
    elif string.startswith('seven'):
        return number + '7' + word_to_num((string[5:]))
    elif string.startswith('eight'):
        return number + '8' + word_to_num((string[5:]))
    elif string.startswith('nine'):
        return number + '9' + word_to_num((string[4:]))
    elif not string:
        return ""
    else:
        raise TypeError


def num_to_word(num):
    """
    Converts a number to a word representing that number.

    Args:
    num (str): A string representing a number.

    Returns:
    str: A string representing the input number in word form.

    Raises:
    IndexError
    """
    if num == '':
        return ''
    return output + digits[num[0]] + num_to_word(num[1:])


def gcd(number1, number2):
    """
    Computes the GCD of two numbers using recursion.

    Args:
    number1 (int): The first integer.
    number2 (int): The second integer.

    Returns:
    int: The GCD of the input integers.

    Raises:
    TypeError
    """
    if number2 == 0:
        return number1
    else:
        return gcd(number2, number1 % number2)


try:
    inputstr1 = str(input("Please enter input 1: "))
    inputnum1 = int(word_to_num(inputstr1))
    inputstr2 = str(input("Please enter input 2: "))
    inputnum2 = int(word_to_num(inputstr2))
    gcd_num = str(gcd(inputnum1, inputnum2))
    print("GCD of given inputs is {}".format(num_to_word(gcd_num)))
except ValueError as valueError:
    print("Please enter a number.")
except TypeError as typeError:
    print("Please enter a number.")
except IndexError as indexError:
    print("Please check the inputs again.")
