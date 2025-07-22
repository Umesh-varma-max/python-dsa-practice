'''
def leader(arr, n):
    max_right = arr[-1]
    print(max_right, end=" ")  # Rightmost is always a leader

    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            print(max_right, end=" ")

# Input
n = int(input())
arr = list(map(int, input().split()))
leader(arr, n)
'''
def leader(arr, n):
    if n == 0:
        return []
    rest = leader(arr[1:], n - 1)
    if all(arr[0] > x for x in arr[1:]):
        return [arr[0]] + rest
    else:
        return rest

n = int(input())
arr = list(map(int, input().split()))
result = leader(arr, n)
print(*result)


