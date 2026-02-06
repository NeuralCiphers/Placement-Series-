
public class DoublyLinkedList {
    
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
    
    // Convert Array to Doubly Linked List
    public static Node arrayToDLL(int[] arr) {
        if (arr.length == 0) {
            return null;
        }
        
        Node head = new Node(arr[0]);
        Node prevNode = head;
        
        for (int i = 1; i < arr.length; i++) {
            Node temp = new Node(arr[i]);
            prevNode.next = temp;
            temp.prev = prevNode;
            prevNode = temp;
        }
        
        return head;
    }
    
    // Insert at Head
    public static Node insertAtHead(Node head, int val) {
        Node newNode = new Node(val);
        
        if (head == null) {
            return newNode;
        }
        
        newNode.next = head;
        head.prev = newNode;
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
        newNode.prev = temp;
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
        newNode.prev = temp;
        
        if (temp.next != null) {
            temp.next.prev = newNode;
        }
        temp.next = newNode;
        
        return head;
    }
    
    // Delete Head
    public static Node deleteHead(Node head) {
        if (head == null) {
            System.out.println("List is empty!");
            return null;
        }
        
        if (head.next == null) {
            return null;
        }
        
        head = head.next;
        head.prev = null;
        return head;
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
        while (temp.next != null) {
            temp = temp.next;
        }
        
        temp.prev.next = null;
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
        
        while (temp != null && count < k) {
            temp = temp.next;
            count++;
        }
        
        if (temp == null) {
            System.out.println("Invalid position!");
            return head;
        }
        
        if (temp.next != null) {
            temp.next.prev = temp.prev;
        }
        
        if (temp.prev != null) {
            temp.prev.next = temp.next;
        }
        
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
            System.out.print(temp.data + " <-> ");
            temp = temp.next;
        }
        System.out.println("NULL");
    }
    
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        Node head = arrayToDLL(arr);
        
        System.out.print("Initial DLL from array: ");
        display(head);
        
        head = insertAtHead(head, 5);
        System.out.print("After inserting at head: ");
        display(head);
        
        head = insertAtTail(head, 60);
        System.out.print("After inserting at tail: ");
        display(head);
        
        head = insertAtK(head, 3, 15);
        System.out.print("After inserting 15 at position 3: ");
        display(head);
        
        head = deleteHead(head);
        System.out.print("After deleting head: ");
        display(head);
        
        head = deleteTail(head);
        System.out.print("After deleting tail: ");
        display(head);
        
        head = deleteAtK(head, 2);
        System.out.print("After deleting node at position 2: ");
        display(head);
    }
}
