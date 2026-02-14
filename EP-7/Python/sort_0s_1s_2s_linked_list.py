# Sort a Linked List of 0s, 1s and 2s
# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

# Definition for singly-linked list.
# class Node:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

class Solution:
    # Approach 1: Count 0s, 1s, 2s and overwrite (Data Replacement)
    def segregate_count(self, head):
        count0, count1, count2 = 0, 0, 0
        temp = head
        
        # Count occurrences of 0, 1, and 2
        while temp:
            if temp.data == 0:
                count0 += 1
            elif temp.data == 1:
                count1 += 1
            else:
                count2 += 1
            temp = temp.next
        
        # Overwrite the linked list with sorted values
        temp = head
        while count0 > 0:
            temp.data = 0
            temp = temp.next
            count0 -= 1
        while count1 > 0:
            temp.data = 1
            temp = temp.next
            count1 -= 1
        while count2 > 0:
            temp.data = 2
            temp = temp.next
            count2 -= 1
        
        return head
    
    # Approach 2: Change Links (Optimal - No Data Modification)
    def segregate(self, head):
        if not head or not head.next:
            return head
        
        # Create dummy nodes for 0s, 1s, and 2s lists
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)
        
        zero = zero_head
        one = one_head
        two = two_head
        
        curr = head
        
        # Traverse and distribute nodes into respective lists
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        
        # Connect the three lists
        # Connect 0s list to 1s list (or 2s list if 1s is empty)
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None
        
        # Return the new head (skip dummy node)
        return zero_head.next

"""
Time Complexity: O(n) - Single/Two traversals of the linked list
Space Complexity: 
  - Approach 1 (Count): O(1)
  - Approach 2 (Change Links): O(1) - Only using constant extra pointers

Example 1:
Input: head = [1,2,2,1,2,0,2,2]
Output: [0,1,1,2,2,2,2,2]

Example 2:
Input: head = [2,2,0,1]
Output: [0,1,2,2]

Note: Approach 2 is preferred when data modification is not allowed.
It maintains the relative order of nodes with the same value.
"""
