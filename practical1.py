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
        return number + '8' + word_to_num((string[8:]))
    elif string.startswith('nine'):
        return number + '9' + word_to_num((string[4:]))
    elif not string:
        return ""
    else:
        return "Please check input again."


def num_to_word(num):
    """
    Converts a number to a word representing that number.
    """
    if num == '':
        return ''
    return output + digits[num[0]] + num_to_word(num[1:])


def gcd(x, y):
    """
    Computes the GCD of two numbers using recursion.
    """
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)


try:
    inputstr1 = str(input("Please enter input 1: "))
    inputnum1 = int(word_to_num(inputstr1))
    inputstr2 = str(input("Please enter input 2: "))
    inputnum2 = int(word_to_num(inputstr2))
    gcd_num = str(gcd(inputnum1, inputnum2))
    print("GCD of given inputs is {}".format(num_to_word(gcd_num)))
except Exception as e:
    print(e)
    print("Please check input again.")
