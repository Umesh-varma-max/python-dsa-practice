def bubble_sort(arr,n):
    for i in range(n - 1, -1, -1):
        swapped = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return(arr)

n=int(input())
arr=list(map(int,input().split()))
a=bubble_sort(arr,n)
print(*a)
