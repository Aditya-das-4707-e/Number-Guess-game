from random import randint

n = randint(1, 100)
a = 0
guess = 0

while (a != n):
    guess = guess + 1

    a = int(input("Guess the number :- "))
    if (a > n):
        print("Lower number please")
    elif (a < n):
        print("Higher number please")
    else:
        break
    
print(f"You guessed the number {n} in {guess} attmepts")
