"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is
a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
letters exactly once.
"""
flag = False

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
    strs = eval(input("Enter inputs: "))
    if len(strs) < 1 or len(strs) > 104:
        raise ValueError("Number of inputs must be between 1 and 104.")
    for item in strs:
        if not (0 <= len(item) <= 100 and item.islower()):
            raise ValueError("Each input must be a lowercase string with length between 1 and 100.")
    anagrams = group_anagrams(strs)
    print(list(anagrams.values()))
except ValueError as valError:
    print(f"Invalid input: {valError}")
except TypeError:
    print("Please enter valid input.")
except IndexError:
    print("Please check the inputs again.")
except Exception:
    print("An error occurred. Please try again.")


