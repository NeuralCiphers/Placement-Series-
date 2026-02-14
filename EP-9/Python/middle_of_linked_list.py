# LeetCode #876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Approach 1: Two Pass - Count nodes first
    def middleNode_two_pass(self, head: ListNode) -> ListNode:
        # First pass: count total nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Second pass: move to middle
        temp = head
        for i in range(count // 2):
            temp = temp.next
        
        return temp
    
    # Approach 2: Fast and Slow Pointer (Tortoise and Hare)
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        # Fast moves 2 steps, slow moves 1 step
        # When fast reaches end, slow is at middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

"""
Time Complexity: 
  - Two Pass: O(n) - Two traversals
  - Fast & Slow: O(n) - Single traversal (but only n/2 iterations)
Space Complexity: O(1) - Only using constant extra space

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node is 3.
List: 1 -> 2 -> 3 -> 4 -> 5
               ^
             middle

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: For even length, return the second middle node.
List: 1 -> 2 -> 3 -> 4 -> 5 -> 6
                    ^
                  middle (2nd middle)

Note: The fast pointer moves twice as fast as the slow pointer.
When fast reaches the end, slow will be at the middle.
For even-length lists, it returns the second middle node.
"""
