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
    None
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
    n = int(input("Enter length of the list: "))
    strs = [str(input("Enter word: ")) for _ in range(n)]
    if 1 <= len(strs) <= 104:
        for i in strs:
            if 0 <= len(i) <= 100:
                print(list(group_anagrams(strs).values()))
            else:
                raise Exception
    else:
        raise Exception
except Exception as e:
    print("Please check inputs again.")
