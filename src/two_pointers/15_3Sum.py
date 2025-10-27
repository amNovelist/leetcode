"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
class Solution(object):
    def binarySearch(self, nums, st, end, value):
        if st > end:
            return -1
        mid = int( (end + st) / 2)
        if nums[mid] == value:
            return mid
        elif nums[mid]> value:
            return self.binarySearch(nums, st, mid-1, value)
        else:
            return self.binarySearch(nums, mid+1, end, value)

    def does_not_exist_in_list(self,val,test_list):
        for data in test_list:
            if data == val:
                return False
        return True

    def threeSum(self, nums):
        l = nums.__len__()
        if l < 2:
            return []

        nums.sort()

        if nums[0] == 0:
            if nums[1] == 0 and nums[2] == 0:
                return [[0,0,0]]

        if nums[l-1] == 0:
            if nums[l-2] == 0 and nums[l-3] == 0:
                return [[0,0,0]]

        distinct_list = []
        for i in range(0, l-2):
            st = i+1
            end = l-1
            val1 = nums[i]

            if val1 > 0:
                return distinct_list

            while st < end:
                sum = nums[st] + nums[end] + val1
                if sum == 0:
                    new_entry = [val1, nums[st], nums[end]]
                    try:
                        distinct_list.index(new_entry)
                    except Exception:
                        distinct_list.append(new_entry)
                    end -= 1
                    st += 1
                elif sum > 0:
                    end -=1
                else:
                    st += 1

        return distinct_list
    #
    # def threeSum_n2lognSolution(self, nums):
    #     len = nums.__len__()
    #     if len <=2:
    #         return []
    #
    #     nums.sort()
    #     min_pos_index = -1
    #     min_neg_index = -1
    #     max_pos_index = -1
    #     max_neg_index = -1
    #     zero_st_index = -1
    #     zero_end_index = -1
    #
    #     if nums[0] < 0:
    #         min_neg_index = 0
    #         max_neg_index = 0
    #     elif nums[0] == 0:
    #         if nums[1] == 0 and nums[2] == 0:
    #             return [[0,0,0]]
    #     else:
    #         return []
    #
    #     if nums[len-1] == 0:
    #         if nums[len-2] == 0 and nums[len-3] == 0:
    #             return [[0,0,0]]
    #     elif nums[len-1] < 0:
    #         return []
    #     else:
    #         max_pos_index = len-1
    #         min_pos_index = len-1
    #
    #     index=1
    #     while index < len:
    #         if nums[index] < 0:
    #             max_neg_index = index
    #         elif nums[index] == 0:
    #             if zero_st_index == -1:
    #                 zero_st_index = zero_end_index = index
    #             else:
    #                 zero_end_index = index
    #         else:
    #             break
    #         index += 1
    #     min_pos_index = index
    #     distinct_list = []
    #
    #     if zero_end_index - zero_st_index >= 2:
    #         distinct_list.append([0,0,0])
    #
    #     for i in range(min_neg_index, max_neg_index+1):
    #         val1 = nums[i]
    #         end = max_pos_index
    #
    #         while end >= min_pos_index:
    #             val2 = nums[end]
    #             sum = val1 + val2
    #             if sum == 0:
    #                 if zero_st_index != -1:
    #                     if self.does_not_exist_in_list([val1, val2, 0], distinct_list):
    #                         distinct_list.append([val1, val2, 0])
    #             elif val1 <= -sum < 0 :
    #                 search_index = self.binarySearch(nums,i+1, max_neg_index,-sum)
    #                 if search_index != -1:
    #                     if self.does_not_exist_in_list([val1, val2, nums[search_index]], distinct_list):
    #                         distinct_list.append([val1, val2, nums[search_index]])
    #             elif 0 < -sum <= val2:
    #                 search_index = self.binarySearch(nums,min_pos_index, end-1,-sum)
    #                 if search_index != -1:
    #                     if self.does_not_exist_in_list([val1, val2, nums[search_index]], distinct_list):
    #                         distinct_list.append([val1, val2, nums[search_index]])
    #             end -= 1
    #     return distinct_list
    #
    # def threeSum_n2lognComplexity(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     len = nums.__len__()
    #     if len <=2:
    #         return []
    #
    #     nums.sort()
    #     if nums[0]> 0:
    #         if nums[1] == 0 and nums[2] == 0:
    #             return [0,0,0]
    #         return []
    #
    #     distinct_results = []
    #     i = 0
    #     while i< len:
    #         j = i+1
    #         while j < len:
    #             value_to_search = -(nums[i]+nums[j])
    #             k = self.binarySearch(nums, j+1, len-1, value_to_search)
    #             if k != -1:
    #                 value_to_append = [nums[i],nums[j],nums[k]]
    #                 distinct_results.append(value_to_append)
    #                 # already_exists = False
    #                 # for res in distinct_results:
    #                 #     if value_to_append == res:
    #                 #         already_exists = True
    #                 #         break
    #                 # if not already_exists:
    #                 #     distinct_results.append(value_to_append)
    #             j += 1
    #         i+=1
    #     result = list(map(list, {tuple(x) for x in distinct_results}))
    #     return result

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1, -1, 2], [-1, 0, 1]]
print(s.threeSum([0,1,1])) # []
print(s.threeSum([0,0,0])) # [[0, 0, 0]]
print(s.threeSum([1,4])) # []
print(s.threeSum([1,2,4])) # []
print(s.threeSum([-1,0,1])) # [[-1,0,1]]
print(s.threeSum([-1,0,1,2,-1,4,9,-9,1,2,5,-5,-3,-2])) # [[-9, 0, 9], [-9, 4, 5], [-5, 0, 5], [-5, 1, 4], [-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1]]