class Solution(object):
    def search(self, nums, target):
        l = 0   
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
             return mid
            elif nums[mid] < target:
             l = mid + 1
            else:
             r = mid - 1
            
        return -1

#example
"""Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4"""