"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""
def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for word in text.split():
        if word.isdigit():  # checks if word is an integer
            numbers.append(int(word))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return char_count, word_count, numbers, total, average

if __name__ == "__main__":
    text = input("Enter some text: ")
    chars, words, numbers, total, avg = analyze_text(text)

    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Numbers found: {numbers}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg:.2f}")
