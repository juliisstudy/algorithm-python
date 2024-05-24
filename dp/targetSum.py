from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, remaining):
            if remaining == 0 and i == len(nums): 
                return 1
            elif i == len(nums):
                return 0
            return backtrack(i+1, remaining + nums[i]) + backtrack(i+1, remaining - nums[i])
            
        
        return backtrack(0,target)