import random
def guess(x):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number:
                guess = int(input(f"Enter the number between 1 and {x}"))
                if (guess > random_number):
                    print("Your guess is too high")
                elif (guess < random_number):
                    print("your guess is too low")
        print(f"Congrats your guess {random_number} is correct")

guess(10)
