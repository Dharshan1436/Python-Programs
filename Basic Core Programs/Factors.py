def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(n)

print(f"Prime factors of {n} are:", *factors)
