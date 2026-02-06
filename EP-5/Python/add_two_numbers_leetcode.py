# LeetCode #2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            sum_val = carry
            
            if l1:
                sum_val += l1.val
                l1 = l1.next
            
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next
        
        return dummy_head.next

"""
Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
Space Complexity: O(max(m, n)) for the result list

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998
"""
