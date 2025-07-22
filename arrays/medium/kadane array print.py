
import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  
    sum = 0
 
    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        if sum < 0:
            sum = 0
    print("The subarray is:",arr[ansStart:ansEnd+1] )
    

 

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)