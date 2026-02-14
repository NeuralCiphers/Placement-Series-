# LeetCode #234: Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Approach 1: Using Extra Space (List)
    def isPalindrome_extra_space(self, head: ListNode) -> bool:
        values = []
        temp = head
        
        # Store all values in list
        while temp:
            values.append(temp.val)
            temp = temp.next
        
        # Check if list is palindrome
        return values == values[::-1]
    
    # Helper function to reverse a linked list
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    # Approach 2: Optimal - Reverse Second Half (O(1) Space)
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle using slow and fast pointers
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        second_half_start = self.reverse_list(slow.next)
        
        # Step 3: Compare first half and reversed second half
        first_half = head
        second_half = second_half_start
        is_palin = True
        
        while second_half:
            if first_half.val != second_half.val:
                is_palin = False
                break
            first_half = first_half.next
            second_half = second_half.next
        
        # Step 4: Restore the list (optional but good practice)
        slow.next = self.reverse_list(second_half_start)
        
        return is_palin

"""
Time Complexity: 
  - Extra Space: O(n) - Store all values + compare
  - Optimal: O(n) - Find middle + reverse + compare
Space Complexity: 
  - Extra Space: O(n) - For storing values
  - Optimal: O(1) - Only using constant extra space

Example 1:
Input: head = [1,2,2,1]
Output: true
Explanation: 1 -> 2 -> 2 -> 1 is a palindrome

Example 2:
Input: head = [1,2]
Output: false
Explanation: 1 -> 2 is not a palindrome

Example 3:
Input: head = [1,2,3,2,1]
Output: true
Explanation: 1 -> 2 -> 3 -> 2 -> 1 is a palindrome

Algorithm (Optimal):
1. Find middle of linked list using slow-fast pointers
2. Reverse the second half of the list
3. Compare first half with reversed second half
4. (Optional) Restore the list by reversing second half again
"""
