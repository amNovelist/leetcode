# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        index = 0
        output = ListNode()
        carry_over = 0
        while l1.next and l2.next:
            node_sum = l1.val + l2.val + carry_over
            remainder = node_sum % 10
            carry_over = node_sum / 10
            output.val = remainder
            
