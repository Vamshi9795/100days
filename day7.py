# Please write a program which asks the user to type in a sentence.
# The program then prints out the first letter of each word in the sentence, 
# each letter on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

word = input("Please type in a sentence: ")
index = 0
length = len(word)

while index < length:
    # Check if the current character is the first letter of a word
    if index == 0 or word[index - 1] == ' ':
        print(word[index])

    index = index + 1

        