def reverse_words(s):
    words = s.split()  # split the string into a list of words
    reversed_words = [word[::-1] for word in words]  # reverse each word
    return ' '.join(reversed_words)  # join the reversed words back into a string
# test the function
input_string = "My name is Ravi"
print(reverse_words(input_string))  # output: "olleH dlroW"