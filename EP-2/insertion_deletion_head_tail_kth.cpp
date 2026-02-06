#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int val) {
        data = val;
        next = NULL;
    }
};

// Insert at Head
Node* insertAtHead(Node* head, int val) {
    Node* newNode = new Node(val);
    newNode->next = head;
    return newNode;
}

// Insert at Tail
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
    return head;
}

// Insert at Kth Position (1-indexed)
Node* insertAtK(Node* head, int k, int val) {
    if (k == 1) {
        return insertAtHead(head, val);
    }
    
    Node* newNode = new Node(val);
    Node* temp = head;
    int count = 1;
    
    while (temp != NULL && count < k - 1) {
        temp = temp->next;
        count++;
    }
    
    if (temp == NULL) {
        cout << "Invalid position!" << endl;
        return head;
    }
    
    newNode->next = temp->next;
    temp->next = newNode;
    return head;
}

// Delete Head
Node* deleteHead(Node* head) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return NULL;
    }
    
    Node* temp = head;
    head = head->next;
    delete temp;
    return head;
}

// Delete Tail
Node* deleteTail(Node* head) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return NULL;
    }
    
    if (head->next == NULL) {
        delete head;
        return NULL;
    }
    
    Node* temp = head;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    
    delete temp->next;
    temp->next = NULL;
    return head;
}

// Delete Kth Node (1-indexed)
Node* deleteAtK(Node* head, int k) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return NULL;
    }
    
    if (k == 1) {
        return deleteHead(head);
    }
    
    Node* temp = head;
    int count = 1;
    
    while (temp != NULL && count < k - 1) {
        temp = temp->next;
        count++;
    }
    
    if (temp == NULL || temp->next == NULL) {
        cout << "Invalid position!" << endl;
        return head;
    }
    
    Node* nodeToDelete = temp->next;
    temp->next = temp->next->next;
    delete nodeToDelete;
    return head;
}

// Display List
void display(Node* head) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return;
    }
    
    Node* temp = head;
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

int main() {
    Node* head = NULL;
    
    // Insert at head
    head = insertAtHead(head, 10);
    head = insertAtHead(head, 20);
    head = insertAtHead(head, 30);
    cout << "After inserting at head: ";
    display(head);
    
    // Insert at tail
    head = insertAtTail(head, 5);
    head = insertAtTail(head, 1);
    cout << "After inserting at tail: ";
    display(head);
    
    // Insert at Kth position
    head = insertAtK(head, 3, 25);
    cout << "After inserting 25 at position 3: ";
    display(head);
    
    // Delete head
    head = deleteHead(head);
    cout << "After deleting head: ";
    display(head);
    
    // Delete tail
    head = deleteTail(head);
    cout << "After deleting tail: ";
    display(head);
    
    // Delete Kth node
    head = deleteAtK(head, 2);
    cout << "After deleting node at position 2: ";
    display(head);
    
    return 0;
}
