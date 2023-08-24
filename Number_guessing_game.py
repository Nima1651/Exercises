import random


system = random.randint(1,6)
for i in range(3):
    print(f"chance ; {i + 1}")
    user = int(input("enter your guess: "))
    if user == system:
        print("Correct!! the chosen number was",system)
    else:
        print("Wrong!")

