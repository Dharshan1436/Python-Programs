import random

def flip_coin(n):
    heads = 0
    tails = 0

    for _ in range(n):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    heads_percentage = (heads / n) * 100
    tails_percentage = 100 - heads_percentage

    print("Heads Percentage:", heads_percentage, "%")
    print("Tails Percentage:", tails_percentage, "%")

flips = int(input("Enter the number of times to flip the coin: "))
flip_coin(flips)
