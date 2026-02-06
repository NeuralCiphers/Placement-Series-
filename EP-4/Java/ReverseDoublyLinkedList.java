public class ReverseDoublyLinkedList {
    
    static class Node {
        int data;
        Node next;
        Node prev;
        
        Node(int val) {
            this.data = val;
            this.next = null;
            this.prev = null;
        }
    }
    
    // Method 1: By Swapping Next and Prev Pointers
    public static Node reverseDLL(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        Node curr = head;
        Node temp = null;
        
        while (curr != null) {
            // Swap prev and next pointers
            temp = curr.prev;
            curr.prev = curr.next;
            curr.next = temp;
            
            // Move to next node (which is now prev due to swap)
            curr = curr.prev;
        }
        
        // temp.prev is the new head (last node we processed)
        if (temp != null) {
            head = temp.prev;
        }
        
        return head;
    }
    
    // Method 2: Recursive Approach
    public static Node reverseDLLRecursive(Node head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        Node newHead = reverseDLLRecursive(head.next);
        
        head.next.next = head;
        head.prev = head.next;
        head.next = null;
        
        return newHead;
    }
    
    // Insert at Tail (Helper function for testing)
    public static Node insertAtTail(Node head, int val) {
        Node newNode = new Node(val);
        
        if (head == null) {
            return newNode;
        }
        
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        
        temp.next = newNode;
        newNode.prev = temp;
        return head;
    }
    
    // Display List
    public static void display(Node head) {
        if (head == null) {
            System.out.println("List is empty!");
            return;
        }
        
        Node temp = head;
        System.out.print("NULL <-> ");
        while (temp != null) {
            System.out.print(temp.data + " <-> ");
            temp = temp.next;
        }
        System.out.println("NULL");
    }
    
    public static void main(String[] args) {
        Node head = null;
        
        // Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
        head = insertAtTail(head, 1);
        head = insertAtTail(head, 2);
        head = insertAtTail(head, 3);
        head = insertAtTail(head, 4);
        head = insertAtTail(head, 5);
        
        System.out.print("Original List: ");
        display(head);
        
        // Reverse the list
        head = reverseDLL(head);
        
        System.out.print("Reversed List: ");
        display(head);
        
        // Reverse again to get original
        head = reverseDLL(head);
        
        System.out.print("Reversed Again: ");
        display(head);
    }
}
