import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

# User choice
user_input = input("Type rock, paper, or scissors\n").lower()
print("The user input:")

# Check user input and print the corresponding choice
if user_input == "rock":
    print(rock)
elif user_input == "scissors":
    print(scissors)
else:
    print(paper)

# Computer input
random_input = random.choice(images)
print(f"The computer input is: {random_input}")

# Logic for determining the winner
if (user_input == "rock" and random_input == rock ) or (user_input == "scissors" and random_input == scissors) or (user_input == "paper" and random_input == paper):
    print(" Its a tie bitch lol")
else:
    if (user_input == "rock" and "scissors" in random_input) or \
       (user_input == "paper" and "rock" in random_input) or \
       (user_input == "scissors" and "paper" in random_input):
        print("You win")
    else:
        print("The computer wins looserrr")
