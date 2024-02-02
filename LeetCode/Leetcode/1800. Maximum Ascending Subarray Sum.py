class Solution(object):
    def maxAscendingSum(self, nums):
       
        maximumsum = nums[0]
        currentsum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
             currentsum += nums[i]
             maximumsum = max(maximumsum, currentsum) 
            else:
             currentsum = nums[i]
            
        return maximumsum
#example
#  nums = [10,20,30,5,10,50]