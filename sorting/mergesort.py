def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Merge the two sorted halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Append remaining elements from left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Append remaining elements from right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy sorted elements back to original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

# ---------------------- Driver Code ------------------------
n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

# 🛑 Input validation
if len(arr) != n:
    print(f"❌ Error: Expected {n} elements but got {len(arr)}.")
    exit()

merge_sort(arr, 0, n - 1)
print("Sorted array:", *arr)
