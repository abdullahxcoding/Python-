import random 

jackpot = random.randint(1,100)
print(jackpot)
guess = int(input("Guess the number :"))

while jackpot != guess:
    if guess > jackpot: 
        print("wrong answer choose the smaller number")
    elif guess < jackpot:
        print("wrong answer choose the larger number")
    guess = int(input("Guess the number :"))

print("Correct answer")