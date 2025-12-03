"""
20. Valid Parentheses
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Stack:
    def __init__(self):
        self.l = []
        self.last_index = -1

    def push(self, value):
        self.l.append(value)
        self.last_index += 1

    def pop(self):
        self.last_index -= 1
        return self.l.pop()

    def peek(self):
        return self.l[self.last_index]

    def isEmpty(self):
        if self.last_index == -1:
            return True
        else:
            return False

class Solution(object):
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.push(char)
            elif char == ')' and (stack.isEmpty() or stack.pop()) != '(':
                return False
            elif char == ']' and (stack.isEmpty() or stack.pop()) != '[':
                return False
            elif char == '}' and (stack.isEmpty() or stack.pop()) != '{':
                return False
        if stack.isEmpty():
            return True
        return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                l.append(char)
                continue

            if len(l) == 0:
                return False

            last_value = l.pop()

            if char == ')' and last_value != '(':
                return False
            elif char == ']' and last_value != '[':
                return False
            elif char == '}' and last_value != '{':
                return False
        if len(l) ==0:
            return True
        return False

s = Solution()
print(s.isValid("((")) # FALSE
print(s.isValid("()")) # TRUE
print(s.isValid("(]")) # FALSE
print(s.isValid("(()([]){})")) #TRUE
print(s.isValid("(()([]){}")) # FALSE
print(s.isValid(")()([]){})")) # FALSE
print(s.isValid("))")) # FALSE
print(s.isValid("{))(([]][}{}")) # FALSE
