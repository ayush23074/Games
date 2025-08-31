import random
low=0
high=1000
guesses=0
number=random.randint(low,high)
Running=False
while Running:
    guess=int(input(f"enter a no. between {low}-{high}:"))
    guesses+=1
    if guess<number:
        print(f"{guess} is too low")
    elif guess>number:
        print(f"{guess} is too High")
    else:
        print(f"{guess} is coorect")
        print(f"You took {guesses} guesses")
print("Thanks for playing")