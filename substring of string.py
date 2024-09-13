# Get the input string from the user
string = input("Enter a string: ")

# Initialize an empty list to store the substrings
substrings = []

# Iterate over each possible length of substring
for length in range(1, len(string) + 1):
    # Iterate over each possible starting index for the substring
    for start in range(len(string) - length + 1):
        # Extract the substring
        substring = string[start:start + length]
        # Add the substring to the list
        substrings.append(substring)

# Print the substrings
print("Substrings of every length:")
for substring in substrings:
    print(substring)