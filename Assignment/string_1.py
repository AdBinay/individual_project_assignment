import string
from collections import Counter
from itertools import permutations
import matplotlib.pyplot as plt

# Function to summarize letters in a string
def summarize_letters(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string.lower()))
    frequency = Counter(filtered_string)
    letter_summary = list(frequency.items())
    return letter_summary

# Function to check if the string has all the letters of the alphabet
def has_all_letters(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string.lower()))
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(filtered_string))

# Function to present descriptive statistics and graphs
def present_statistics(letter_summary):
    letters, frequencies = zip(*letter_summary)
    print("Descriptive Statistics:")
    print(f"Total Unique Letters: {len(letters)}")
    print(f"Most Frequent Letter: {max(letter_summary, key=lambda x: x[1])}")
    print(f"Least Frequent Letter: {min(letter_summary, key=lambda x: x[1])}")
    plt.bar(letters, frequencies)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency in the String')
    plt.show()

# Function to sort letters and remove duplicates
def sort_letters(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string.lower()))
    sorted_unique_letters = sorted(set(filtered_string))
    return ''.join(sorted_unique_letters)

# Function to generate anagrams
def generate_anagrams(input_string):
    filtered_string = ''.join(filter(str.isalpha, input_string.lower()))
    anagrams = set(''.join(p) for p in permutations(filtered_string))
    return list(anagrams)

# Input string from the user
input_string = input("Enter a string: ")

# Summarize letters
letter_summary = summarize_letters(input_string)
print("Letter Summary (Letter: Frequency):")
for letter, freq in letter_summary:
    print(f"{letter}: {freq}")

# Check if the string has all letters of the alphabet
if has_all_letters(input_string):
    print("The string contains all the letters of the alphabet.")
else:
    print("The string does not contain all the letters of the alphabet.")

# Present descriptive statistics and graph
present_statistics(letter_summary)

# Sort letters and remove duplicates
sorted_letters = sort_letters(input_string)
print("Sorted Letters (Unique):", sorted_letters)

# Generate anagrams
anagrams = generate_anagrams(input_string)
print(f"Anagrams ({len(anagrams)} found):", anagrams)
