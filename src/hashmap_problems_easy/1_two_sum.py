from collections import defaultdict

"""
1. Two Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


"""

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_nums = defaultdict(list)
        index = 0
        for num in nums:
            list_nums[num].append(index)
            index +=1

        index = 0
        for num in nums:
            remaining_value = target - num

            if list_nums[remaining_value]:
                if len(list_nums[remaining_value]) == 1:
                    if list_nums[remaining_value][0] != index:
                        return [index, list_nums[remaining_value][0]]
                elif len(list_nums[remaining_value]) > 1:
                    return [index, list_nums[remaining_value][1]]

            if list_nums[num]:
                list_nums.__delitem__(num)
            index += 1
        return [0,0]

x = Solution()
print(x.twoSum( [3,0,1,-3,5, -4, -3, 0, -19],9))

"""SOlution complexity: O(N), Time complexity: O(N), RUntime: 11ms"""