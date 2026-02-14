# LeetCode #328: Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even  # Save the head of even list
        
        while even and even.next:
            odd.next = even.next   # Connect odd to next odd
            odd = odd.next
            
            even.next = odd.next   # Connect even to next even
            even = even.next
        
        odd.next = even_head  # Connect odd list to even list
        
        return head

"""
Time Complexity: O(n) - Single traversal of the linked list
Space Complexity: O(1) - Only using constant extra space

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Explanation: Odd indexed nodes: 1,3,5 | Even indexed nodes: 2,4

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Note: The first node is considered odd, and the second node is even, and so on.
We group all odd nodes together followed by all even nodes.
"""
