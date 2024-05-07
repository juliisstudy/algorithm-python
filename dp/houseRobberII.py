# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

def rob(self,nums:List[int])->int:
    if(len(nums)) ==0 or nums is None:
        return 0
    if len(nums) == 1:
        return max(self.rob_simple(nums[:-1]),self.rob_simple(nums[1:]))

def rob_simple(self,nums:List[int])->int:
    t1 = 0
    t2 = 0
    for current in nums:
        temp = t1
        t1 = max(current+t2,t1)
        t2 = temp
    
    return t1