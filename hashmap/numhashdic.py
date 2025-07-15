arr = list(map(int, input().split()))
hash_table = {}

for num in arr:
    if num in hash_table:
        hash_table[num] += 1
    else:
        hash_table[num] = 1

print(hash_table)
