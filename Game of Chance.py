import random

win_freq = 0
lose_freq = 0

for i in range(1000):
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    diceSum = dice1 + dice2
    if diceSum == 3 or diceSum == 5 or diceSum == 7 or diceSum == 9 or diceSum == 11:
        win_freq += 1
    else:
        lose_freq += 1

if win_freq > lose_freq:
    print("You won the game.")
elif win_freq < lose_freq:
    print("You lost the game")
else:
    print("It's a Draw")

print(f"Your winning frequency is {win_freq}")
print(f"Your losing frequency is {lose_freq}")