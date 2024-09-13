# Get the input string from the user
string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
char_freq = {}

# Iterate over each character in the string
for char in string:
    # If the character is already in the dictionary, increment its count
    if char in char_freq:
        char_freq[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        char_freq[char] = 1

# Print the character frequencies
print("Character Frequencies:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}")