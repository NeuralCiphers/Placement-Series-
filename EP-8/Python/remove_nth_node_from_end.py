# LeetCode #19: Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Approach 1: Two Pass - Find length first
    def removeNthFromEnd_two_pass(self, head: ListNode, n: int) -> ListNode:
        # First pass: find the length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        # Edge case: removing the head
        if n == length:
            return head.next
        
        # Second pass: find the (length - n)th node
        temp = head
        for i in range(1, length - n):
            temp = temp.next
        
        # Remove the nth node from end
        temp.next = temp.next.next
        
        return head
    
    # Approach 2: One Pass - Two Pointers (Fast & Slow)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next

"""
Time Complexity: 
  - Two Pass: O(n) - Two traversals
  - One Pass: O(n) - Single traversal
Space Complexity: O(1) - Only using constant extra space

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: Remove 4 (2nd node from end)

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Note: The one-pass approach uses two pointers with a gap of n nodes.
When fast reaches the end, slow is at the node before the one to be removed.
"""
