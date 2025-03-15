import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

sessior=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images=[rock,paper,sessior]
print("Welcome to all this computer based game [Rock,Paper,Sessior]")

user_choice=input("choose 1 for rock :\n"
                  "choose 2 for paper :\n"
                  "choose 3 for sessior :\n")
if user_choice>=3 and user_choice<4:
     print(images[user_choice])

# if user_choice==1:
#      print(f"You choose rock: ",{rock})
# elif user_choice==2:
#     print(f"You choose paper: ",{paper})
# elif user_choice==3:
#      print(f"You choose sessior: ",{sessior})

     
     
     
computer_choice=random.randint(1,3)
if computer_choice>=1 and computer_choice<4:
     print(images[computer_choice])
# if computer_choice==1:
#      print(f"computer choose rock: ",{rock})
# elif computer_choice==2:
#     print(f"computer choose paper: ",{paper})
# elif computer_choice==3:
#      print(f"computer choose sessior: ",{sessior})

     
if user_choice == computer_choice:
     print("It's a tie!")
elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
     print("You win!")
else:
     print("Computer wins!")