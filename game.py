import random
print("0 refers Rock")
print("1 refers Scissors")
print("2 refers paper ")
user=int(input("Enter number in 0,1,2  "))
print(f"user enterd {user}")
computer=random.randint(0,2)
print(f"computer enterd {computer}")
if 0<=user<=2 and 0<=computer<=2:
    if user==computer:
        print("draw")
    elif user==2 and computer==0:
        print("user win the game ")
    elif user==0 and computer==2:
        print("computer win the game ")
    elif user>computer:
        print("computer win the game ")
    elif user<computer:
        print("user win the game ")
else:
    print('user enterd wrong value')