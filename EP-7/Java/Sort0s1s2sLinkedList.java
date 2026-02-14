// Sort a Linked List of 0s, 1s and 2s
// https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

// Definition for singly-linked list.
class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Solution {
    // Approach 1: Count 0s, 1s, 2s and overwrite (Data Replacement)
    public Node segregateCount(Node head) {
        int count0 = 0, count1 = 0, count2 = 0;
        Node temp = head;
        
        // Count occurrences of 0, 1, and 2
        while (temp != null) {
            if (temp.data == 0) count0++;
            else if (temp.data == 1) count1++;
            else count2++;
            temp = temp.next;
        }
        
        // Overwrite the linked list with sorted values
        temp = head;
        while (count0-- > 0) {
            temp.data = 0;
            temp = temp.next;
        }
        while (count1-- > 0) {
            temp.data = 1;
            temp = temp.next;
        }
        while (count2-- > 0) {
            temp.data = 2;
            temp = temp.next;
        }
        
        return head;
    }
    
    // Approach 2: Change Links (Optimal - No Data Modification)
    public Node segregate(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        // Create dummy nodes for 0s, 1s, and 2s lists
        Node zeroHead = new Node(-1);
        Node oneHead = new Node(-1);
        Node twoHead = new Node(-1);
        
        Node zero = zeroHead;
        Node one = oneHead;
        Node two = twoHead;
        
        Node curr = head;
        
        // Traverse and distribute nodes into respective lists
        while (curr != null) {
            if (curr.data == 0) {
                zero.next = curr;
                zero = zero.next;
            } else if (curr.data == 1) {
                one.next = curr;
                one = one.next;
            } else {
                two.next = curr;
                two = two.next;
            }
            curr = curr.next;
        }
        
        // Connect the three lists
        // Connect 0s list to 1s list (or 2s list if 1s is empty)
        zero.next = (oneHead.next != null) ? oneHead.next : twoHead.next;
        one.next = twoHead.next;
        two.next = null;
        
        // Get the new head (skip dummy node)
        return zeroHead.next;
    }
}

/*
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
*/
