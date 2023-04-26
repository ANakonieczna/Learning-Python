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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

images = [rock, paper, scissors]

print("Your choice:")
if choice >= 0 and choice <= 2:
    print(images[choice])
else:
    print("Wrong choice.")

compchoice = random.randint(0, 2)

print("Computer's choice:")
print(images[compchoice])

if choice == compchoice:
    print("It's a draw.")
elif (choice == 0 and compchoice == 2) or (choice == 1 and compchoice == 0) or (choice == 2 and compchoice == 1):
    print("You win.")
else:
    print("You lose.")
