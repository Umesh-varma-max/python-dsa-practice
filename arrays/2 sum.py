# worst  case O(n*2),O(n)

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
a=Solution()
nums=list(map(int,input().split()))
k=int(input())
b=a.twoSum(nums,k)
print(b)

#best case O(n),O(n)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return seen[diff], i
            seen[num] = i
a=Solution()
nums=list(map(int,input().split()))
k=int(input())
b=print(a.twoSum(nums,k))

#two pointers
def twosum(nums,k):
    l=0
    r=len(nums)-1
    while l<r:
        s=nums[l]+nums[r]
        if s==k:
            return l,r
        elif  s<k:
            l+=1
        else:
            r-=1
nums=list(map(int,input().split()))
k=int(input())
b=print(twosum(nums,k))



