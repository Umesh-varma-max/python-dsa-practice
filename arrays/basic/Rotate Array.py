class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n 
        nums[:] = nums[-k:] + nums[:-k]
        return nums
