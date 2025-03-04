import random
target=random.randint(1,100)
while True:
    userchoice=int(input("Enter your choice number: "))
    if userchoice==target:
        print("Success your choice is correct !!")
        break
    elif userchoice>target:
        print("You guess a incorrect number...please guess a smaller number")
    elif userchoice<target:
        print("You guess a incorrect number...please guess a larger number")
    else:
        print("Please guess number in the range")
print("....Game over.....")