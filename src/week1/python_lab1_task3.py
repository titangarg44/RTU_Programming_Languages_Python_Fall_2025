"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""
def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    char_count = len(text)  # total characters
    word_count = len(text.split())  # total words
    contains_python = "python" in text.lower()  # check case-insensitive
    return char_count, word_count, contains_python

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    chars, words, has_python = analyze_sentence(sentence)
    print(f"Total characters: {chars}")
    print(f"Total words: {words}")
    print(f"Contains 'Python': {'Yes' if has_python else 'No'}")
