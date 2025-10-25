"""
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l == 1:
            return s[0]
        if l ==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        curr = 0
        prev = 0
        nxt = curr+1
        max_len = 1
        max_substr = s[0]
        while curr < l:
            flag=True
            while nxt < l and prev >= 0 and (s[curr] == s[nxt] or s[nxt] == s[prev]):
                if flag and s[curr] == s[nxt]:
                    max_substr= s[curr: nxt+1] if max_len < (nxt - curr + 1) else max_substr
                    max_len = nxt - curr + 1 if max_len < (nxt - curr + 1) else max_len
                    nxt += 1
                elif s[prev] == s[nxt]:
                    flag = False
                    max_substr = s[prev: nxt +1] if max_len < (nxt - prev + 1) else max_substr
                    max_len = nxt - prev + 1 if max_len < (nxt - prev + 1) else max_len
                    prev -=1
                    nxt += 1
                else:
                    prev +=1
                    nxt -= 1
                    break
            curr = nxt
            nxt = curr+1
            prev = curr -1
        return max_substr

s=Solution()
print(s.longestPalindrome("malayalam"))
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("ccd"))
print(s.longestPalindrome("xaabacxcabaaxcabaax")) #xaabacxcabaax
print(s.longestPalindrome("abbcccbbbcaaccbababcbcabca")) #xaabacxcabaax
print(s.longestPalindrome("bananas")) #anana
print(s.longestPalindrome("abadada"))
print(s.longestPalindrome("ababababa"))#xaabacxcabaax



