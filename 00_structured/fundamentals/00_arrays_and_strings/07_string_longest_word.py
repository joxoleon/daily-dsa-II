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

def longest_word(sentence: str) -> str:
    pass

if __name__ == "__main__":
    assert longest_word("The quick brown fox") == "quick"
    assert longest_word("Hello world!") == "Hello"
    assert longest_word("Can't stop, won't stop.") == "Can't"
    assert longest_word("Hi!") == "Hi!"
    assert longest_word("This is a test sentence.") == "sentence."
    assert longest_word("Equal tie ties") == "Equal"
    assert longest_word("a ab abc abcd") == "abcd"
    assert longest_word("apple banana watermelon") == "watermelon"
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
