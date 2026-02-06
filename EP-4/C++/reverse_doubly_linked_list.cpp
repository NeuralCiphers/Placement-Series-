#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;
    
    Node(int val) {
        data = val;
        next = NULL;
        prev = NULL;
    }
};

// Method 1: By Swapping Next and Prev Pointers
Node* reverseDLL(Node* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }
    
    Node* curr = head;
    Node* temp = NULL;
    
    while (curr != NULL) {
        // Swap prev and next pointers
        temp = curr->prev;
        curr->prev = curr->next;
        curr->next = temp;
        
        // Move to next node (which is now prev due to swap)
        curr = curr->prev;
    }
    
    // temp->prev is the new head (last node we processed)
    if (temp != NULL) {
        head = temp->prev;
    }
    
    return head;
}

// Method 2: Using Stack (Less efficient but easier to understand)
Node* reverseDLLUsingStack(Node* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }
    
    Node* curr = head;
    
    // Store all data values in a temporary array/stack
    while (curr != NULL) {
        // Swap next and prev
        Node* temp = curr->next;
        curr->next = curr->prev;
        curr->prev = temp;
        
        // Move to previous node
        head = curr;
        curr = temp;
    }
    
    return head;
}

// Method 3: Recursive Approach
Node* reverseDLLRecursive(Node* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }
    
    Node* newHead = reverseDLLRecursive(head->next);
    
    head->next->next = head;
    head->prev = head->next;
    head->next = NULL;
    
    return newHead;
}

// Insert at Tail (Helper function for testing)
Node* insertAtTail(Node* head, int val) {
    Node* newNode = new Node(val);
    
    if (head == NULL) {
        return newNode;
    }
    
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    
    temp->next = newNode;
    newNode->prev = temp;
    return head;
}

// Display List
void display(Node* head) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return;
    }
    
    Node* temp = head;
    cout << "NULL <-> ";
    while (temp != NULL) {
        cout << temp->data << " <-> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

int main() {
    Node* head = NULL;
    
    // Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4 <-> 5
    head = insertAtTail(head, 1);
    head = insertAtTail(head, 2);
    head = insertAtTail(head, 3);
    head = insertAtTail(head, 4);
    head = insertAtTail(head, 5);
    
    cout << "Original List: ";
    display(head);
    
    // Reverse the list
    head = reverseDLL(head);
    
    cout << "Reversed List: ";
    display(head);
    
    // Reverse again to get original
    head = reverseDLL(head);
    
    cout << "Reversed Again: ";
    display(head);
    
    return 0;
}
