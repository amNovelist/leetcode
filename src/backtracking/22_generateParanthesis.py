"""
22. Generate Parentheses
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""

class Solution(object):
    def generateParanthesis(self, n):
        result = set()

        def addbracket(open_count, closed_count, s):
            if len(s) == 2*n:
                result.add(s)
                return

            if open_count < n:
                # Add Open Bracket , increment open bracket by 1
                addbracket(open_count+1, closed_count, s +"(")

            if closed_count < open_count:
                # Add Closed Bracket, increment closed bracket by 1
                addbracket(open_count, closed_count+1, s +")")

        addbracket(0,0,"")
        return list(result)
s=Solution()
n=8
print(s.generateParanthesis(n))
print(len(s.generateParanthesis(n)))