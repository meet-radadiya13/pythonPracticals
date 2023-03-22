"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is
a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
letters exactly once.
"""


def group_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return anagrams


n = int(input("Enter length of the list: "))
strs = [input("Enter word: ") for _ in range(n)]
print(list(group_anagrams(strs).values()))
