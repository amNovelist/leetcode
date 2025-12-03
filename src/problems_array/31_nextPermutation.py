"""
31. Next Permutation
Medium
Topics
premium lock icon
Companies
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        value = nums[-1]
        value_arr = [0]*101

        full_rev = True
        index = len(nums) - 1
        value_arr[nums[index]] += 1
        for num in nums[-2::-1]:
            if num >= value:
                value_arr[num] += 1
                index -= 1
                value = num
                continue
            else:
                value_arr[num] += 1
                index -= 1
                full_rev = False
                break

        i=index+1
        x = nums[index]
        j = x+1
        while j <= 100:
            if value_arr[j] > 0:
                nums[index] = j
                value_arr[j] -= 1
                break
            j += 1

        if full_rev:
            i = 0

        for j in range(0, 101):
            while value_arr[j] > 0:
                nums[i] = j
                value_arr[j] -= 1
                i+= 1
        print(nums)

    def nextPermutation_copied(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If pivot found, find number just bigger and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        print(nums)

s = Solution()
s.nextPermutation([1,2,5,4,3]) # [1, 3, 2, 4, 5]
s.nextPermutation([1,2,3,4,5]) # [1, 2, 3, 5, 4]
s.nextPermutation([5,4,3,2,1]) # [1, 2, 3, 4, 5]
s.nextPermutation([5,3,4,2,1]) # [5, 4, 1, 2, 3]
s.nextPermutation([7, 7, 7]) # [7, 7, 7]
s.nextPermutation([1, 2]) # [2, 1]
s.nextPermutation([1, 3, 2]) # [2, 1, 3]
s.nextPermutation([16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20])