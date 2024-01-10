# Please make an extended version of the previous program, 
# which prints out all the substrings which are at least three characters long, 
# and which begin with the character specified by the user. 
# You may assume the input string is at least three characters long.


# Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot
# Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# while True:
#     word = input("enter the word: ")
#     character = input("enter the character you wanna find: ")
#     length = len(word)
#     print(f"length of word is {length}")
#     index = word.find(character)
#     print(f"index is {index}")
#     three_char = index + 3
#     print(f"the three added index is {three_char}")
#     if index >= 0 and index+3 <len(word):
#         print(f" The 3 characters is {word[index:three_char]}")
#     else:
#         print(" the index is  out of bounds")
while True:
    word = input("enter the word: ")
    character = input("enter the character :")
    first_occurance= word.find(character)
    if first_occurance == -1:
        print("second occuace not found")
    else:
        second_occurace = word.find(character, first_occurance+1)
        if second_occurace == -1:
            print("second occurace not found")
        else:
            print(f"second_occurace found at{second_occurace}" )
        
        
        