import random

def generate_random_number(N):
    return random.randint(1, N)

def collect_coupons(N):
    coupons_collected = []
    count = 0

    while len(set(coupons_collected)) < N:
        coupon = generate_random_number(N)
        coupons_collected.append(coupon)
        count += 1

    return count

N = int(input("Enter the number of distinct coupon numbers: "))

total_random_numbers_needed = collect_coupons(N)

print("Total random numbers needed to collect", N, "distinct coupon numbers:", total_random_numbers_needed)
