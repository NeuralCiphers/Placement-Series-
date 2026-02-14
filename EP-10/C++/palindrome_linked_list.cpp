// LeetCode #234: Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

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
    // Approach 1: Using Extra Space (Stack or Array)
    bool isPalindrome_ExtraSpace(ListNode* head) {
        vector<int> values;
        ListNode* temp = head;
        
        // Store all values in array
        while (temp != NULL) {
            values.push_back(temp->val);
            temp = temp->next;
        }
        
        // Check if array is palindrome
        int left = 0, right = values.size() - 1;
        while (left < right) {
            if (values[left] != values[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    // Helper function to reverse a linked list
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* curr = head;
        
        while (curr != NULL) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        
        return prev;
    }
    
    // Approach 2: Optimal - Reverse Second Half (O(1) Space)
    bool isPalindrome(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return true;
        }
        
        // Step 1: Find the middle using slow and fast pointers
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Step 2: Reverse the second half
        ListNode* secondHalfStart = reverseList(slow->next);
        
        // Step 3: Compare first half and reversed second half
        ListNode* firstHalf = head;
        ListNode* secondHalf = secondHalfStart;
        bool isPalin = true;
        
        while (secondHalf != NULL) {
            if (firstHalf->val != secondHalf->val) {
                isPalin = false;
                break;
            }
            firstHalf = firstHalf->next;
            secondHalf = secondHalf->next;
        }
        
        // Step 4: Restore the list (optional but good practice)
        slow->next = reverseList(secondHalfStart);
        
        return isPalin;
    }
};

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
