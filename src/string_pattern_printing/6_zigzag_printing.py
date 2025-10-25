"""
6. Zigzag Conversion
Medium
Topics
premium lock icon
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
PINASGYAHRPI
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        op =""
        l = s.__len__()
        inc = inc2 = numRows + numRows -2
        counter = 0
        if l <= numRows:
            return s
        if numRows == 1:
            return s
        for r in range(0,numRows):
            c = r
            while c < l:
                op=op+s[c]
                if inc2 > 0 and inc2 < inc and c+inc2 < l:
                    op=op+s[c+inc2]
                c = c + inc
                counter += 1
            inc2 = inc2 - 2
        return op
s = Solution()
print(s.convert("PAYPALISHIRING",3) == "PAHNAPLSIIGYIR")
print(s.convert("A",1) == "A")
print(s.convert("123456",5) == "123465")
print(s.convert("PAYPALISHIRING",4) == "PINALSIGYAHRPI")
s.convert("PAYPALISHIRING",5) #PAHNAPLSIIGYIR #PAHNAPLSIIGYIR
#
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17
# 3
# 0,4,8,12,16,1,5,9,13,17,2,6,10,14,3,7,11,15
# 0,6,12,1,7,13,2,8,14,3,9,15,4,10,16,5,
#
# 14 = 4 = 7
# 14 = 3 = 7
#
# 00         08         16
# 01      07 09      15 17
# 02    06   10    14   18
# 03  05     11  13     19
# 04         12         20
#
# 21, 5, 9
#
#
# 0 + 8 + 8
# 1 + 7 + 9 + 15 + 17
# 2 + 6 + 10 + 14 + 16
# 3 + 5 + 11 + 13 +
#
#
#
#
#
# 00       06       12
# 01    05 07    11 13
# 02 04    08 10    14
# 03       09       15
#
# 15,4, 7
#
#
#
# Row = 5
# N + (N-1)) / total = 4/5 = 1
# 21 => 21/5 * 3 = 4 * 3 = 12
