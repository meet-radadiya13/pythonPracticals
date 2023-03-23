"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generate_braces(n, memo={}):
    """
    Generates all possible valid combinations of n pairs of parentheses.

    Args:
    n (int): The number of pairs of parentheses to generate.

    Returns:
    list: A list of strings representing all valid combinations of n pairs of parentheses.

    Raises:
    None
    """
    if n in memo:
        return memo[n]
    output = []
    if n == 0:
        output.append('')
    else:
        for i in range(n):
            for left in generate_braces(i, memo):
                for right in generate_braces(n - i - 1, memo):
                    output.append('({}){}'.format(left, right))
    memo[n] = output
    return output


n = int(input("Enter n: "))
if 1 <= n <= 8:
    print(generate_braces(n))
else:
    print("Please enter number between 1 and 8")
