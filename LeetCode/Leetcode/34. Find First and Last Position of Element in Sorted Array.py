class Solution(object):
  def searchRange(self, nums, target):
    def SearchLeft(nums, target):
      left, right = 0, len(nums) - 1
      i = -1
      while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
          right = mid - 1
        else:
          left = mid + 1  
        if nums[mid] == target:
          i = mid
      return i

    def SearchRight(nums, target):
      left, right = 0, len(nums) - 1
      i = -1
      while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
          left = mid + 1
        else:
          right = mid - 1
        if nums[mid] == target:  
          i = mid
      return i
      
    left_index = SearchLeft(nums, target)
    right_index = SearchRight(nums, target)
    
    return [left_index, right_index]

#example
"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]





 """