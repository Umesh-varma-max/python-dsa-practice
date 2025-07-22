#O(n),O(1)
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
A=Solution()
nums=list(map(int,input().split()))
A.singleNumber(nums)

'''
#O(N),O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for key, val in freq.items():
            if val == 1:
                return key
A=Solution()
nums=list(map(int,input().split()))
A.singleNumber(nums)
'''