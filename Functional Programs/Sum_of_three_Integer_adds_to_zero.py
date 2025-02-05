def find_triplets(arr):
    n = len(arr)
    result = set()

    arr.sort()

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                result.add((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    print("Number of distinct triplets:", len(result))
    print("Distinct triplets:")
    for triplet in result:
        print(triplet)

# Input
N = int(input("Enter the number of integers (N): "))
arr = list(map(int, input("Enter the integers: ").split()))

# Find and print triplets
find_triplets(arr)
