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

import random
game=[rock,paper,scissors]
computer_choice=random.randint(0,2)
number_of_choice=int(input("What do you choose? 0=rock, 1=paper, 2=scissors "))

if number_of_choice>=3 or number_of_choice<0:
  print("Invalid number, please try again")
else:
  print("User Choice:")
  print(game[number_of_choice])

  print("Computer Choice:")
  print(game[computer_choice])

  if number_of_choice==0:
    if computer_choice==0:
      print("\nThat's a draw")
    elif computer_choice==1:
      print("\nYou have lost")
    else:
      print("\nYou have won")
  elif number_of_choice==1:
    if computer_choice==0:
      print("\nYou have won")
    elif computer_choice==1:
      print("\nThat's a draw")
    else:
      print("\nYou have lost")
  else:
    if computer_choice==0:
      print("\nYou have lost")
    elif computer_choice==1:
      print("\nYou have won")
    else:
      print("\nThat's a draw")

