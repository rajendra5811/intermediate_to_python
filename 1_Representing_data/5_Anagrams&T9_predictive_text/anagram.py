from wordsets import english_words, english_words_small


def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """
    #### ADD YOUR CODE BELOW ####
    # Create a dictionary mapping the canonical representation of a word to all anagrams of those letters.
    lookup = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in lookup:
            lookup[key] = set()
        lookup[key].add(word)

    # Search the lookup table for the queried letters.
    search = ''.join((sorted(letters)))
    return lookup.get(search, set())

    #### ADD YOUR CODE ABOVE ####


if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ").lower().strip()
        for anagram in find_anagrams(letters, english_words_small):
            print(anagram)
