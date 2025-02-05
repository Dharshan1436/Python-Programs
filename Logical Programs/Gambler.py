import random

def gambler_simulation(stake, goal, trials):
    wins = 0
    bets = 0

    for _ in range(trials):
        current_stake = stake
        while 0 < current_stake < goal:
            bets += 1
            if random.random() < 0.5:  # 50% chance to win a bet
                current_stake += 1
            else:
                current_stake -= 1
        
        if current_stake == goal:
            wins += 1

    win_percentage = (wins / trials) * 100
    loss_percentage = 100 - win_percentage

    print(f"Number of Wins: {wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
    print(f"Average Bets per Trial: {bets / trials:.2f}")


# Get input values from the user
stake = int(input("Enter the initial stake ($): "))
goal = int(input("Enter the goal ($): "))
trials = int(input("Enter the number of trials: "))

# Run the simulation
gambler_simulation(stake, goal, trials)
