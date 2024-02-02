class Solution(object):
    def findPeakElement(self, nums):
       r = len(nums) - 1
       l = 0
       while  l < r:
           mid = (r + l) // 2

           if nums[mid] < nums[mid+1]:
               l= mid + 1

           else:
               r=mid

       return l
"""
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.






"""