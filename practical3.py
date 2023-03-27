"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is
a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
letters exactly once.
"""


def group_anagrams(lst):
    """
    Groups the words in the given list into sets of anagrams.

    Args:
    lst (list): A list of words.

    Returns:
    dict: A dictionary mapping sorted strings of characters to lists of words that are anagrams of each other.

    Raises:
    IndexError
    """
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams


try:
    list_length = int(input("Enter length of the list: "))
    strs = [str(input("Enter word: ")) for _ in range(list_length)]
    if 1 <= len(strs) <= 104:
        for i in strs:
            if 0 <= len(i) <= 100:
                output = list(group_anagrams(strs).values())
            else:
                raise ValueError
    else:
        raise ValueError
    print(output)
except ValueError as valueError:
    print("Please enter a number with length less than 100.")
except TypeError as typeError:
    print("Please enter a number.")
except IndexError as indexError:
    print("Please check the inputs again.")

