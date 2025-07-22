#brute force O(n^2),O(1)
def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")

 #optimal O(n),O(1)
def issorted(arr, n): 
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            print("unsorted")
            return
    print("sorted")

n = int(input())
arr = list(map(int, input().split()))
issorted(arr, n)
