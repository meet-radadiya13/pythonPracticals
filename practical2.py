"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generate_braces(n, memo={}):
    """
    The code generates all possible combinations of well-formed parentheses given an input n (number of pairs of
    parentheses). It uses a recursive approach where it generates all combinations of well-formed parentheses for
    values less than n and then combines them in all possible ways to generate combinations for n. For further
    optimization code uses memoization, which stores the results for each value of n in a dictionary, to reduce the
    number of recursive calls and improve the overall runtime.
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
