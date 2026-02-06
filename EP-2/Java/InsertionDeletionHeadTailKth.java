public class InsertionDeletionHeadTailKth {
    
    static class Node {
        int data;
        Node next;
        
        Node(int val) {
            this.data = val;
            this.next = null;
        }
    }
    
    // Insert at Head
    public static Node insertAtHead(Node head, int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        return newNode;
    }
    
    // Insert at Tail
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
        return head;
    }
    
    // Insert at Kth Position (1-indexed)
    public static Node insertAtK(Node head, int k, int val) {
        if (k == 1) {
            return insertAtHead(head, val);
        }
        
        Node newNode = new Node(val);
        Node temp = head;
        int count = 1;
        
        while (temp != null && count < k - 1) {
            temp = temp.next;
            count++;
        }
        
        if (temp == null) {
            System.out.println("Invalid position!");
            return head;
        }
        
        newNode.next = temp.next;
        temp.next = newNode;
        return head;
    }
    
    // Delete Head
    public static Node deleteHead(Node head) {
        if (head == null) {
            System.out.println("List is empty!");
            return null;
        }
        return head.next;
    }
    
    // Delete Tail
    public static Node deleteTail(Node head) {
        if (head == null) {
            System.out.println("List is empty!");
            return null;
        }
        
        if (head.next == null) {
            return null;
        }
        
        Node temp = head;
        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
        return head;
    }
    
    // Delete Kth Node (1-indexed)
    public static Node deleteAtK(Node head, int k) {
        if (head == null) {
            System.out.println("List is empty!");
            return null;
        }
        
        if (k == 1) {
            return deleteHead(head);
        }
        
        Node temp = head;
        int count = 1;
        
        while (temp != null && count < k - 1) {
            temp = temp.next;
            count++;
        }
        
        if (temp == null || temp.next == null) {
            System.out.println("Invalid position!");
            return head;
        }
        
        temp.next = temp.next.next;
        return head;
    }
    
    // Display List
    public static void display(Node head) {
        if (head == null) {
            System.out.println("List is empty!");
            return;
        }
        
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("NULL");
    }
    
    public static void main(String[] args) {
        Node head = null;
        
        // Insert at head
        head = insertAtHead(head, 10);
        head = insertAtHead(head, 20);
        head = insertAtHead(head, 30);
        System.out.print("After inserting at head: ");
        display(head);
        
        // Insert at tail
        head = insertAtTail(head, 5);
        head = insertAtTail(head, 1);
        System.out.print("After inserting at tail: ");
        display(head);
        
        // Insert at Kth position
        head = insertAtK(head, 3, 25);
        System.out.print("After inserting 25 at position 3: ");
        display(head);
        
        // Delete head
        head = deleteHead(head);
        System.out.print("After deleting head: ");
        display(head);
        
        // Delete tail
        head = deleteTail(head);
        System.out.print("After deleting tail: ");
        display(head);
        
        // Delete Kth node
        head = deleteAtK(head, 2);
        System.out.print("After deleting node at position 2: ");
        display(head);
    }
}
