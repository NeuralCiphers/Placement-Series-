// LeetCode #234: Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

import java.util.ArrayList;
import java.util.List;

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    // Approach 1: Using Extra Space (ArrayList)
    public boolean isPalindromeExtraSpace(ListNode head) {
        List<Integer> values = new ArrayList<>();
        ListNode temp = head;
        
        // Store all values in list
        while (temp != null) {
            values.add(temp.val);
            temp = temp.next;
        }
        
        // Check if list is palindrome
        int left = 0, right = values.size() - 1;
        while (left < right) {
            if (!values.get(left).equals(values.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    // Helper function to reverse a linked list
    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        return prev;
    }
    
    // Approach 2: Optimal - Reverse Second Half (O(1) Space)
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        
        // Step 1: Find the middle using slow and fast pointers
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Reverse the second half
        ListNode secondHalfStart = reverseList(slow.next);
        
        // Step 3: Compare first half and reversed second half
        ListNode firstHalf = head;
        ListNode secondHalf = secondHalfStart;
        boolean isPalin = true;
        
        while (secondHalf != null) {
            if (firstHalf.val != secondHalf.val) {
                isPalin = false;
                break;
            }
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        
        // Step 4: Restore the list (optional but good practice)
        slow.next = reverseList(secondHalfStart);
        
        return isPalin;
    }
}

/*
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
*/
