#include <iostream>
#include <vector>
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

// Convert Array to Doubly Linked List
Node* arrayToDLL(vector<int>& arr) {
    if (arr.empty()) {
        return NULL;
    }
    
    Node* head = new Node(arr[0]);
    Node* prev = head;
    
    for (int i = 1; i < arr.size(); i++) {
        Node* temp = new Node(arr[i]);
        prev->next = temp;
        temp->prev = prev;
        prev = temp;
    }
    
    return head;
}

// Insert at Head
Node* insertAtHead(Node* head, int val) {
    Node* newNode = new Node(val);
    
    if (head == NULL) {
        return newNode;
    }
    
    newNode->next = head;
    head->prev = newNode;
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
    newNode->prev = temp;
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
    newNode->prev = temp;
    
    if (temp->next != NULL) {
        temp->next->prev = newNode;
    }
    
    temp->next = newNode;
    return head;
}

// Insert Before a Given Node
Node* insertBeforeNode(Node* head, Node* node, int val) {
    if (node == NULL) {
        cout << "Node is NULL!" << endl;
        return head;
    }
    
    Node* newNode = new Node(val);
    
    if (node->prev == NULL) {
        // Inserting before head
        return insertAtHead(head, val);
    }
    
    Node* prevNode = node->prev;
    prevNode->next = newNode;
    newNode->prev = prevNode;
    newNode->next = node;
    node->prev = newNode;
    
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
    
    if (head != NULL) {
        head->prev = NULL;
    }
    
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
    while (temp->next != NULL) {
        temp = temp->next;
    }
    
    temp->prev->next = NULL;
    delete temp;
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
    
    while (temp != NULL && count < k) {
        temp = temp->next;
        count++;
    }
    
    if (temp == NULL) {
        cout << "Invalid position!" << endl;
        return head;
    }
    
    if (temp->prev != NULL) {
        temp->prev->next = temp->next;
    }
    
    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }
    
    delete temp;
    return head;
}

// Delete a Given Node (Not head)
void deleteNode(Node* node) {
    if (node == NULL) {
        cout << "Node is NULL!" << endl;
        return;
    }
    
    if (node->prev != NULL) {
        node->prev->next = node->next;
    }
    
    if (node->next != NULL) {
        node->next->prev = node->prev;
    }
    
    delete node;
}

// Display List Forward
void displayForward(Node* head) {
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

// Display List Backward
void displayBackward(Node* head) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return;
    }
    
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    
    cout << "NULL <-> ";
    while (temp != NULL) {
        cout << temp->data << " <-> ";
        temp = temp->prev;
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
    displayForward(head);
    
    // Insert at tail
    head = insertAtTail(head, 5);
    head = insertAtTail(head, 1);
    cout << "After inserting at tail: ";
    displayForward(head);
    
    // Insert at Kth position
    head = insertAtK(head, 3, 25);
    cout << "After inserting 25 at position 3: ";
    displayForward(head);
    
    // Display backward
    cout << "List in reverse: ";
    displayBackward(head);
    
    // Delete head
    head = deleteHead(head);
    cout << "After deleting head: ";
    displayForward(head);
    
    // Delete tail
    head = deleteTail(head);
    cout << "After deleting tail: ";
    displayForward(head);
    
    // Delete Kth node
    head = deleteAtK(head, 2);
    cout << "After deleting node at position 2: ";
    displayForward(head);
    
    return 0;
}
