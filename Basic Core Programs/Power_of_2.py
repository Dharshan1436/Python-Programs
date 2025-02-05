def print_powers_of_2(n):
    if 0 <= n < 31:
        for i in range(n + 1):
            print(f"2^{i} = {2**i}")
    else:
        print("Please enter a number between 0 and 30.")

n = int(input("Enter the power value N (0 to 30): "))
print_powers_of_2(n)
