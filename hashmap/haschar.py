'''
s = input()

hash_table = {}
for ch in s:
    if ch in hash_table:
        hash_table[ch] += 1
    else:
        hash_table[ch] = 1

for key in hash_table:
    print(f"{key}: {hash_table[key]}")

'''
'''
s = input()

# 26 letters in lowercase English alphabet
hash_table = [0] * 26

for ch in s:
    if 'a' <= ch <= 'z':  # Only count lowercase letters
        hash_table[ord(ch) - ord('a')] += 1

for i in range(26):
    if hash_table[i] > 0:
        print(f"{chr(i + ord('a'))}: {hash_table[i]}")
'''      

s = input("Enter a string: ")
target = input("Enter the character to find: ")

hash_table = {}
for ch in s:
    hash_table[ch] = hash_table.get(ch, 0) + 1

print(f"{target} occurs {hash_table.get(target, 0)} times")
