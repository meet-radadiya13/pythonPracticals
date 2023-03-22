"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generate_braces(n):
    output = []
    if n == 0:
        output.append('')
    else:
        for i in range(n):
            for left in generate_braces(i):
                for right in generate_braces(n - i - 1):
                    output.append('({}){}'.format(left, right))
    return output


n = int(input("Enter n: "))
if 1 <= n <= 8:
    print(generate_braces(n))
else:
    print("Please enter number between 1 and 8")
