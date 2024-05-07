# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

def rob(self,nums:List[int])->int:
    n = len(nums)
    if n ==1:
        return nums[0]
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1],nums[i]+dp[i-2])
    
    return dp[-1]