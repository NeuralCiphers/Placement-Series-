public class ArrayToLL {
    
    static class Node {
        int data;
        Node next;
        
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    
    public static Node arrToLL(int[] arr) {
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
    
    public static int print(Node head) {
        Node temp = head;
        int cnt = 0;
        while (temp != null) {
            cnt++;
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        return cnt;
    }
    
    public static void main(String[] args) {
        int[] arr = {12, 13, 1, 3, 5};
        Node head = arrToLL(arr);
        int cnt = print(head);
        System.out.println("\nTotal number of nodes: " + cnt);
    }
}
