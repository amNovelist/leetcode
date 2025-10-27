"""
14. Longest Common Prefix
Easy
Topics
premium lock icon
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = len(strs[0])
        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)

        common_str = ""
        for i in range(0, min_len):
            val = strs[0][i]
            for s in strs:
                if i < len(s) and val == s[i]:
                    continue
                else:
                    return common_str
            common_str = common_str + val

        return common_str

    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_val = strs[0]

        for s in strs[1:]:
            min_len = min(len(s),len(common_val))
            if len(common_val) > min_len:
                common_val = common_val[0:min_len]

            for i in range(0, min_len):
                if s[i] != common_val[i]:
                    if i > 0:
                        common_val = common_val[0:i]
                        break
                    else:
                        return ""
        return common_val


st = Solution()
print(st.longestCommonPrefix(["flower","flow","flight"]))
print(st.longestCommonPrefix(["dog","racecar","car"]))
print(st.longestCommonPrefix(["ab", "a"]))
