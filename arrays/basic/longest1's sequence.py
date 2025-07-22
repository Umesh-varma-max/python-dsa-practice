from typing import List  # ✅ import this

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = []
        l = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                l += 1
            else:
                c.append(l)
                l = 0
        c.append(l)
        return max(c)

# Test the function
if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print("Max consecutive 1s:", s.findMaxConsecutiveOnes(nums))
