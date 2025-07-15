arr = list(map(int, input().split()))

# Define hash size based on expected input range
MAX = max(arr) + 1
hash_table = [0] * MAX

# Count frequency
for num in arr:
    hash_table[num] += 1

# Print frequency
for i in range(MAX):
    if hash_table[i] > 0:
        print(f"{i}: {hash_table[i]}")
