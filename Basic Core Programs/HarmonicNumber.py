def harmonic_number(n):
    if n != 0:
        harmonic_sum = 0
        for i in range(1, n + 1):
            harmonic_sum += 1 / i
        return harmonic_sum
    else:
        return "N should not be zero."

n = int(input("Enter the harmonic value N (N != 0): "))
result = harmonic_number(n)

if isinstance(result, str):
    print(result)
else:
    print(f"The {n}th harmonic number is: {result:.4f}")
