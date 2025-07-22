O(n),O(n)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        r=[]
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            else:
                n.append(nums[i])
                
        for i in range(len(p)):
            r.append(p[i])
            r.append(n[i])
        return r
            
        
        