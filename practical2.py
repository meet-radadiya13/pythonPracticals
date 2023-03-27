"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generate_braces(number, memo={}):
    """
    Generates all possible valid combinations of n pairs of parentheses.

    Args:
    n (int): The number of pairs of parentheses to generate.

    Returns:
    list: A list of strings representing all valid combinations of n pairs of parentheses.

    Raises:
    IndexError
    """
    if number in memo:
        return memo[number]
    output = []
    if number == 0:
        output.append('')
    else:
        for i in range(number):
            for left in generate_braces(i, memo):
                for right in generate_braces(number - i - 1, memo):
                    output.append('({}){}'.format(left, right))
    memo[number] = output
    return output

try:
    number = int(input("Enter number to generate braces: "))
    if 1 <= number <= 8:
        print(generate_braces(number))
    else:
        raise ValueError
except ValueError as valueError:
    print("Please enter a number between 1 and 8.")
except TypeError as typeError:
    print("Please enter a number.")
except IndexError as indexError:
    print("Please check the inputs again.")

