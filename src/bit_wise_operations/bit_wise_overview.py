import math


def bitwise_multiplication(a,b):
    result = 0
    while b > 0:
        if b & 1:
            result += a
        a = a << 1
        b = b >> 1
    return result
#
# print(bitwise_multiplication(19,5))
# print(bitwise_multiplication(11,3))
# print(bitwise_multiplication(8,4))
# print(bitwise_multiplication(100,80))
# print(bitwise_multiplication(12,25))
# print(bitwise_multiplication(19,1))

def bitwise_division(a,b):
    numerator = 0
    upper_limit = i = math.floor(math.log(a,2))
    while i in range(upper_limit,-1,-1) and a > 0:
        val = b << i
        if val <= a:
            a = a-val
            numerator += (1 << i)
        i=i-1
    return numerator

print(bitwise_division(100,5))
print(bitwise_division(43,5))
print(bitwise_division(44,9))
print(bitwise_division(12,12))
print(bitwise_division(12,41))

