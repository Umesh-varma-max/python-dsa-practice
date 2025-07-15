#boyyer mooree O(N),O(1)
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:            # pick a new candidate
                candidate = num
            count += 1 if num == candidate else -1

        # because the majority element is guaranteed to exist,
        # candidate is the answer without a second pass
        return candidate
s=Solution()
nums=list(map(int,input().split()))
print(s.majorityElement(nums))