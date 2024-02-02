class Solution(object):
    def findLucky(self, arr):

        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        lucky = -1
        for num, freq in count.items():
            if num == freq:
             lucky = max(lucky, num)

        return lucky

""" Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2."""