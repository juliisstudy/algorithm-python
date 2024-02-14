def maxProduct(self,nums:List[int])->int:
    if len(nums) ==0:
        return 0
    max = nums[0]
    min = nums[0]
    result = max
    for i in range(1,len(nums)):
        curr = nums[i]
        temp_max = max(curr,max*curr,min*curr)
        min = min(curr,max*curr,min*curr)
        max = temp_max
        result =max(max,result)
    return result
