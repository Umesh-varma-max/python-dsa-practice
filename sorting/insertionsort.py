def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift larger element to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct spot
    return arr

# Input
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = insertion_sort(arr, n)
print(*sorted_arr)
 