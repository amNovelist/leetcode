"""
17. Letter Combinations of a Phone Number
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key_map = {"2": ["a","b","c"],
                   "3": ["d","e","f"],
                   "4": ["g","h","i"],
                   "5": ["j","k","l"],
                   "6": ["m","n","o"],
                   "7": ["p","q","r","s"],
                   "8": ["t","u","v"],
                   "9": ["w","x","y","z"]}

        output_combinations = []
        for digit in digits:
            keys = key_map.get(digit)
            if digit == 1 or output_combinations == []:
                output_combinations = keys
            else:
                temp_op = []
                for output_combination in output_combinations:
                    for key in keys:
                        temp_op.append(output_combination + key)
                output_combinations = temp_op
        return output_combinations


s = Solution()
print(s.letterCombinations("456"))