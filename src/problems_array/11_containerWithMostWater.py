"""
https://leetcode.com/problems/container-with-most-water/
11. Container With Most Water
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        st = 0
        end = l-1
        maxArea = 0
        while st < end:
            temp = min(height[st], height[end]) * (end-st)
            if maxArea < temp:
                maxArea = temp
            if height[st] > height[end]:
                end -= 1
            else:
                st += 1
        return maxArea

s=Solution()

print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(s.maxArea([1,1])) # 1
print(s.maxArea([1,5,3,2,4,5,2,1,2,3]))
print(s.maxArea([1,7,9,11,4,3,1,8,5,13,4,9,6,3,1]))
# print(s.maxArea())
# print(s.maxArea())
# print(s.maxArea())
# print(s.maxArea())
# print(s.maxArea())
# print(s.maxArea())