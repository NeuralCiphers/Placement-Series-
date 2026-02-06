public class InsertionDeletionLL {
    
    static class Node {
        int data;
        Node next;
        
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    
    static class Insertion {
    
    public Node insertAtHead(Node head, int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        return newNode;
    }
    
    public Node insertAtTail(Node head, int data) {
        Node newNode = new Node(data);
        if (head == null) return newNode;
        
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
        return head;
    }
    
    public Node insertAtKthPos(Node head, int k, int data) {
        Node newNode = new Node(data);
        if (k == 1) {
            return insertAtHead(head, data);
        }
        
        Node temp = head;
        Node prev = null;
        while (temp != null && k > 1) {
            k--;
            prev = temp;
            temp = temp.next;
        }
        prev.next = newNode;
        newNode.next = temp;
        return head;
    }
    
    public Node arrToLL(int[] arr) {
        if (arr.length == 0) return null;
        
        Node head = new Node(arr[0]);
        Node mover = head;
        
        for (int i = 1; i < arr.length; i++) {
            Node temp = new Node(arr[i]);
            mover.next = temp;
            mover = temp;
        }
        return head;
    }
    
    public void print(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
    
    static class Deletion {
    
    public Node deleteHead(Node head) {
        if (head == null) return null;
        return head.next;
    }
    
    public Node deleteTail(Node head) {
        if (head == null || head.next == null) return null;
        
        Node temp = head;
        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
        return head;
    }
    }
    
    public static void main(String[] args) {
        int[] arr = {12, 13, 1, 3, 5};
        Insertion it = new Insertion();
        Node head = it.arrToLL(arr);
        
        head = it.insertAtHead(head, 5);
        it.print(head);
        System.out.println();
        
        head = it.insertAtTail(head, 10);
        it.print(head);
        System.out.println();
        
        head = it.insertAtKthPos(head, 3, 45);
        it.print(head);
        System.out.println();
        
        Deletion dt = new Deletion();
        head = dt.deleteHead(head);
        it.print(head);
        System.out.println();
        
        head = dt.deleteTail(head);
        it.print(head);
    }
}
}
