def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        part = partition(arr, low, high)
        # Recursively sort the elements before and after partition
        quicksort(arr, low, part - 1)
        quicksort(arr, part + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1        # Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element to correct position

    # Place pivot after the last smaller element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

# Apply quicksort
quicksort(arr, 0, n - 1)

# Output
print("Sorted array:")
print(*arr)
 
'''
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        qs(arr, low, pIndex - 1)
        qs(arr, pIndex + 1, high)

def quick_sort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

# Main
arr = [4, 6, 2, 5, 7, 9, 1, 3]
print("Before Using Quick Sort:")
print(*arr)

sorted_arr = quick_sort(arr)
print("After Using Quick Sort:")
print(*sorted_arr)
'''  
