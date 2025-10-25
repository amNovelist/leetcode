"""
7. Reverse Integer
Medium
Topics
premium lock icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-2^31 <= x <= 2^31 - 1
"""
import math
class Solution(object):
    def reverse_long(self, x):
        """
        :type x: int
        :rtype: int
        2147483647
        Limit:  -2147483648 to 2147483647
        """

        if x > -10 and x < 10:
            return x

        neg_flag = False
        if x < 0:
            neg_flag = True

        max_val = int(math.pow(2,31)) - 1
        num_digits = 0
        while int(x / pow(10,num_digits)) != 0:
            num_digits += 1

        if num_digits == 10 and (abs(x) % 10) > 2:
            return 0

        sum = 0
        counter = num_digits-1
        x = abs(x)
        for pow_i in range(1,num_digits+1):
            rem = x % 10
            sum = sum + rem * pow(10,counter)
            if sum > max_val:
                return 0
            x = int(x / 10)
            counter -= 1
            if x == 0:
                break

        if neg_flag:
            return -sum
        return sum

    def reverse_simplified(self, x):
        """
        :type x: int
        :rtype: int
        2147483647
        Limit:  -2147483648 to 2147483647
        """

        if -10 < x < 10:
            return x

        neg_flag = False
        if x < 0:
            neg_flag = True
            x = abs(x)

        max_val = int(math.pow(2,31)) - 1
        num_digits = 0
        while int(x / pow(10,num_digits)) != 0:
            num_digits += 1

        if num_digits == 10 and (x % 10) > 2:
            return 0

        st = 0
        end = num_digits

        for pow_i in range(1,num_digits):
            rem = int(int(x % pow(10,pow_i)) / int(pow(10,pow_i -1)))
            num = int((x / pow(10,num_digits-pow_i)) % 10)
            x = x - num*(pow(10,num_digits-pow_i))-rem*(pow(10,st))
            x = x + num *(pow(10,st)) + rem*(pow(10,end-1))
            st += 1
            end -= 1
            rem_max_val = int(int(max_val % pow(10,pow_i)) / int(pow(10,pow_i -1)))
            if x > max_val:
                return 0
            if st >= end:
                break

        if neg_flag:
            return -x
        return x
        #
        # is_x_eq_10_dig = False
        # counter = 0
        # sum = 0
        # for i in range(9,-1,-1):
        #     num =  int(abs(x) / pow(10,i))
        #     if num <= 0:
        #         continue
        #     else:
        #         val = int(num % 10)
        #         if i == 9:
        #             is_x_eq_10_dig = True
        #         # if is_x_eq_10_dig:
        #         #     if val > int(abs(max_val) % 10):
        #         #         return 0
        #         #     else:
        #         #         max_val = abs(int(max_val / 10))
        #         if is_x_eq_10_dig:
        #             if num > int(abs(max_val) % pow(10,9-i+1)):
        #                 return 0
        #             #else:
        #             #    max_val = abs(int(max_val / 10))
        #         sum = sum + val * pow(10,counter)
        #         counter += 1
        #
        # if neg_flag:
        #     return -sum
        # else:
        #     return sum


    # 205 => 502
    # 205/ 10^3 => 0 => 0
    # 205/ 10^2 => 2 => 0 + 2 * (10 ^ 0) = 2
    # 205 / 10^1 => 20 % 10 => 0 => 2 + 0 * ( 10 ^ 1) => 2 + 0
    # 205 / 1 => 205 % 10 => 5 => 2 + 5 * ( 10 ^ 2) => 2 + 500 = 502



s = Solution()
print(s.reverse_simplified(-1463847412))
print(s.reverse_simplified(2147483649)) # 0
print(s.reverse_simplified(2147483648)) # 0
print(s.reverse_simplified(2147483647)) # 0
print(s.reverse_simplified(-2147483647)) # 0
print(s.reverse_simplified(-2147483648)) # 0
print(s.reverse_simplified(-2147483649)) # 0
print(s.reverse_simplified(-214483649)) #-946384412
print(s.reverse_simplified(-102709)) #-907201
print(s.reverse_simplified(-987654321)) #-123456789
print(s.reverse_simplified(-5))  # -5
print(s.reverse_simplified(0)) # 0
print(s.reverse_simplified(10)) # 1
print(s.reverse_simplified(-9)) # -9
print(s.reverse_simplified(-123)) # -321
print(s.reverse_simplified(123)) # 321
print(s.reverse_simplified(7463847412)) # 2147483647
print(s.reverse_simplified(8463847412)) # 0
print(s.reverse_simplified(-6463847412)) # -2147483646
print(s.reverse_simplified(-7463847412)) # -2147483647
print(s.reverse_simplified(-8463847412)) # 0
print(s.reverse_simplified(-9463847412)) # 0
print(s.reverse_simplified(-2147483412)) # large: -2147483648 on rotation: -2143847412
# print(int(-2047483648 / 100000000))
# print(int(-2047483648 % 10))

"""
-2147483412


"""