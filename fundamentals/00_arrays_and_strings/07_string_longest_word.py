# [ Name: Find the Longest Word in a Sentence ]  [ Category: strings ]  [ Topic: scanning ]  [ Weight: 4 ]

"""
Problem Description:
Given a string sentence containing words separated by spaces, return the longest word.
If multiple words are tied for the longest, return the first such word in the sentence.
The input may contain punctuation or mixed-case letters.
Assume the sentence is non-empty and words are separated by single spaces.

Constraints:
- Input: a string with 1 <= len(sentence) <= 10^4
- Words contain only alphabetic characters and/or punctuation.

Example:
Input: "Hello world!" -> Output: "Hello"
"""
import string

def longest_word(sentence: str) -> str:
    punct = set(string.punctuation)
    words = sentence.split()

    best_word = words[0]
    best_len = len(words[0].strip(string.punctuation))

    for w in words[1:]:
        cleaned = w.strip(string.punctuation)
        L = len(cleaned)

        if L > best_len:
            best_len = L
            best_word = w

    return best_word
    

if __name__ == "__main__":
    assert longest_word("The quick brown fox") == "quick"
    assert longest_word("Hello world!") == "Hello"
    assert longest_word("Can't stop, won't stop.") == "Can't"
    assert longest_word("Hi!") == "Hi!"
    assert longest_word("This is a test sentence.") == "sentence."
    assert longest_word("Equal tie ties") == "Equal"
    assert longest_word("a ab abc abcd") == "abcd"
    assert longest_word("apple banana watermelon") == "watermelon"
    print("All tests passed.")
