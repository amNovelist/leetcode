"""
Median of Two Sorted Arrays
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from xmlrpc.client import MININT, MAXINT


class Solution(object):
    def is_odd(self, val):
        return True if val % 2 != 0 else False

    def get_median(self, val1, val2, is_odd):
        if is_odd:
            return val2
        else:
            return ((val1 + val2) / 2.0)

    def findNextBiggest(self, arr, val, st, end):
        if st >= end:
            if arr[st] > val:
                return st
            else:
                return st + 1
        mid = int((end + st ) / 2)

        if arr[mid] > val:
            return self.findNextBiggest (arr, val, st, mid-1)
        else:
            return self.findNextBiggest (arr, val, mid+1, end)


    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        total_len = l1 + l2
        is_odd = self.is_odd(total_len)
        median = int(total_len / 2)

        if l1 == 0:
            return self.get_median(nums2[median-1], nums2[median], is_odd)

        if l2 == 0:
            return self.get_median(nums1[median-1], nums1[median], is_odd)

        st1 = st2 = 0
        e1 = l1 - 1
        e2 = l2 - 1

        if nums1[st1] >= nums2[e2]:
            if l1 > l2:
                return self.get_median(nums1[median-l2-1], nums1[median-l2], is_odd)
            elif l1 == l2:
                return self.get_median(nums2[e2], nums1[st1], is_odd)
            else:
                return self.get_median(nums2[median-1], nums2[median], is_odd)
        elif nums2[st2] >= nums1[e1]:
            if l1 > l2:
                return self.get_median(nums1[median-1], nums1[median], is_odd)
            elif l1 == l2:
                return self.get_median( nums1[e2],nums2[st1], is_odd)
            else:
                return self.get_median(nums2[median-l1-1], nums2[median-l1], is_odd)

        counter = 0
        val1 = -10000001
        val2 = -10000001
        while counter <= median and st1 <= e1 and st2 <= e2:
            m1 = int((e1 + st1) / 2)
            m2 = int((e2 + st2) / 2)

            if nums1[m1] > nums2[m2]:
                ind = self.findNextBiggest(nums1, nums2[m2], st1, m1-1)
                if ind > 0 and val2 < nums1[ind-1]:
                    val2 = nums1[ind-1]
                elif m2 > 0 and val2 < nums2[m2-1]:
                    val2 = nums2[m2-1]
                # else:
                #     val2 = val1
                val1 = nums2[m2]
                counter += ind - st1
                counter += m2 + 1 - st2
                if m2 + 1 >= l2:
                    if median-counter >= 1:
                        return self.get_median(nums1[median-counter-1+ind],nums1[median-counter+ind], is_odd)
                    elif median-counter == 0 :
                        return self.get_median(val1,nums1[counter-median+ind], is_odd)
                    else:
                        return self.get_median(val2,val1, is_odd)
                else:
                    st2 = m2 + 1
                    e2 = st2 + (median - counter) if st2 + (median - counter) < l2 else l2-1
                st1 = ind if ind < l1 else l1 - 1
                e1 = st1 + (median - counter) if st1 + (median - counter) < l1 else l1-1
            elif nums1[m1] < nums2[m2]:
                ind = self.findNextBiggest(nums2, nums1[m1], st2, m2-1)
                if ind > 0 and val2 < nums2[ind-1]:
                    val2 = nums2[ind-1]
                elif m1 > 0 and val2 < nums1[m1-1]:
                    val2 = nums1[m1-1]
                # else:
                #     val2 = val1

                val1 = nums1[m1]
                counter += ind - st2
                counter += m1 + 1 - st1

                if m1 + 1 >= l1:
                    if median-counter >= 1:
                        return self.get_median(nums2[median-counter-1+ind],nums2[median-counter+ind], is_odd)
                    elif median-counter == 0:
                        return self.get_median(val1,nums2[counter-median+ind], is_odd)
                    else:
                        return self.get_median(val2,val1, is_odd)
                else:
                    st1 = m1 + 1
                    e1 = st1 + (median - counter) if st1 + (median - counter) < l1 else l1-1
                st2 = ind if ind < l2 else l2 - 1
                e2 = st2 + (median - counter) if st2 + (median - counter) < l2 else l2-1
            else:
                
                val1 = nums1[m1]
                counter += ind - st2
                counter += m1 + 1 - st1

                if m1 + 1 >= l1:
                    if median-counter >= 1:
                        return self.get_median(nums2[median-counter-1+ind],nums2[median-counter+ind], is_odd)
                    elif median-counter == 0:
                        return self.get_median(val1,nums2[counter-median+ind], is_odd)
                    else:
                        return self.get_median(val2,val1, is_odd)
                else:
                    st1 = m1 + 1
                    e1 = st1 + (median - counter) if st1 + (median - counter) < l1 else l1-1
                st2 = ind if ind < l2 else l2 - 1
                e2 = st2 + (median - counter) if st2 + (median - counter) < l2 else l2-1

        if counter>median:
            return self.get_median(val2,val1, is_odd)

        return -1

    def solutionUsingOn(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        is_odd = False if (l1+l2) % 2 == 0 else True
        median = int((l1 + l2) / 2)
        if l1 == 0:
            return self.get_median(nums2[median-1], nums2[median], is_odd)
        if l2 == 0:
            return self.get_median(nums1[median-1], nums1[median], is_odd)
        counter = 0

        val1 = None
        val2 = None

        i=j=0
        while i<l1 and j < l2 and counter <= median:
            if nums1[i] <= nums2[j]:
                val2 = val1
                val1 = nums1[i]
                i += 1
                counter+=1
            else:
                val2 = val1
                val1 = nums2[j]
                j +=1
                counter+=1

        if i==l1 and j<l2 and counter < median:
            return self.get_median(nums2[counter-i-j], nums2[counter-i-j+1], is_odd)

        if j==l2 and i<l1 and counter < median:
            return self.get_median(nums1[counter-i-j], nums1[counter-i-j+1], is_odd)

        if counter -1 == median:
            return self.get_median(val2, val1, is_odd)
        return -1

    def worstCaseSoln(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        total_len = l1 + l2
        op = [None] * total_len
        i=j=0
        while i <l1 and j < l2:
            if nums1[i] < nums2[j]:
                op[i+j] = nums1[i]
                i+=1
            else:
                op[i+j] = nums2[j]
                j+=1
        if j < l2 and i == l1:
            for k in range(j, l2):
                op[i+k] = nums2[k]

        if i < l1 and j == l2:
            for k in range(i, l1):
                op[j+k] = nums1[k]

        is_odd = False if (l1+l2) % 2 == 0 else True
        median = int((l1 + l2) / 2)

        return self.get_median(op[median-1], op[median], is_odd)


            # if counter == median-1:
            #     return self.get_median(nums2[j], nums1[i], is_odd)

"""
Cases:
A=[1,2,3]
B=[99,100,101,109,111]

Op: 99.5

A=[1,2,3,4,5,6]
B=[99,100]

Op:4.5

A=[1,2,3,4,5]
B=[]
Op:3

A=[]
B=[1,2,3,4,5,6]
Op: 3

A=[1,2,3,3,4,5,6,7,8]
B=[1,100,200,300]

Op: 4

"""

# 5
# A=[1,2,3,3,4,5,6,7,8]
# B=[1,100,200,300]

# 5.5
# A=[3]
# B=[1,2,4,5,6,7,8,9,10]

#99.5
# A=[1,2,3]
# B=[99,100,101,109,111]
#
# A=[1,2,3,4,5]
# B=[]

#3.5
# A=[]
# B=[1,2,3,4,5,6]

# 100
# B=[99,100,101,109,111]
# A=[1,2,3,1000]

#2.5
# A=[1,3]
# B=[2,7]

# 2.5
# A=[2]
# B=[1,3,4]

#5.5
# A=[4,6,7,8]
# B=[1,2,3,5,9,10]

# 3.0
A=[2,2,4,4]
B=[2,2,4,4]
x = Solution()
print(x.findMedianSortedArrays(A,B))
print(x.findMedianSortedArrays(B,A))