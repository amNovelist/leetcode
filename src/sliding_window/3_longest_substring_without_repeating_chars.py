"""
3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st_index = 0
        temp_map = {}
        curr_index = 0
        max_len = 0
        curr_len = 0
        for char in s:
            char_existing_index = temp_map.get(char)
            if char_existing_index is None or  char_existing_index < st_index:
                temp_map[char] = curr_index
                curr_len += 1
            else:
                temp_map[char] = curr_index
                st_index = char_existing_index + 1
                curr_len = curr_index - st_index + 1

            if curr_len > max_len:
                max_len = curr_len

            curr_index+=1

        print(f"{s}: {max_len}")

x = Solution()
x.lengthOfLongestSubstring("abcabcbb") # 3
x.lengthOfLongestSubstring("bbbbb") # 1
x.lengthOfLongestSubstring("pwwkew") # 3
x.lengthOfLongestSubstring("dvdf") # 3
x.lengthOfLongestSubstring("ckilbkd") # 5
x.lengthOfLongestSubstring("tmmzuxt") # 5 > WRONG
x.lengthOfLongestSubstring("jbpnbwwd") # 4
x.lengthOfLongestSubstring("anviaj") # 5