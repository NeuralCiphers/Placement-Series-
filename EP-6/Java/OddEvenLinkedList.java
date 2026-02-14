// LeetCode #328: Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;  // Save the head of even list
        
        while (even != null && even.next != null) {
            odd.next = even.next;   // Connect odd to next odd
            odd = odd.next;
            
            even.next = odd.next;   // Connect even to next even
            even = even.next;
        }
        
        odd.next = evenHead;  // Connect odd list to even list
        
        return head;
    }
}

/*
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
*/
