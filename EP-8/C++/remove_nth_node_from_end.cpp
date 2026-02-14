// LeetCode #19: Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    // Approach 1: Two Pass - Find length first
    ListNode* removeNthFromEnd_TwoPass(ListNode* head, int n) {
        // First pass: find the length
        int length = 0;
        ListNode* temp = head;
        while (temp != NULL) {
            length++;
            temp = temp->next;
        }
        
        // Edge case: removing the head
        if (n == length) {
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }
        
        // Second pass: find the (length - n)th node
        temp = head;
        for (int i = 1; i < length - n; i++) {
            temp = temp->next;
        }
        
        // Remove the nth node from end
        ListNode* toDelete = temp->next;
        temp->next = temp->next->next;
        delete toDelete;
        
        return head;
    }
    
    // Approach 2: One Pass - Two Pointers (Fast & Slow)
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        
        ListNode* fast = dummy;
        ListNode* slow = dummy;
        
        // Move fast pointer n+1 steps ahead
        for (int i = 0; i <= n; i++) {
            fast = fast->next;
        }
        
        // Move both pointers until fast reaches the end
        while (fast != NULL) {
            fast = fast->next;
            slow = slow->next;
        }
        
        // Remove the nth node from end
        ListNode* toDelete = slow->next;
        slow->next = slow->next->next;
        delete toDelete;
        
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};

/*
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
*/
