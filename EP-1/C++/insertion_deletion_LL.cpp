#include<iostream>
#include<vector>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    Node(int data){
        this->data=data;
        this->next=NULL;
    }
};
class Insertion{
    public:
    Node* insertAtHead(Node* head, int data){
        Node* newNode=new Node(data);
        newNode->next=head;
        head=newNode;
        return head;
    }
    Node* insertAtTail(Node* head , int data){
        Node* newNode=new Node(data);
        Node* temp=head;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newNode;
        return head;
    }
    Node* insertATKthPos(Node* head , int k , int data){
        Node* newNode=new Node(data);
        if(k==1){
            return insertAtHead(head,data);  
        }
        Node* temp=head;
        Node* prev=NULL;
        while(temp!=NULL && k>1){
            k--;
            prev=temp;
            temp=temp->next;
        }
        prev->next=newNode;
        newNode->next=temp;
        return head;
    }
    Node* arrToLL(vector<int>&arr){
    int n=arr.size();
    Node* head=new Node(arr[0]);
    Node* mover=head;
    for(int i=1;i<n;i++){
        Node* temp = new Node(arr[i]);
        mover->next=temp;
        mover=temp;
    }
    return head;
}
void print(Node* head){
    Node* temp=head;
    while(temp!=NULL){
       
        cout<<temp->data<<" ";
        temp=temp->next;
    }   
}
};
class Deletion{
    public:
    Node* deleteHead(Node* head){
        Node* temp=head;
        head=head->next;
        delete(temp);
        return head;
    }
    Node* deleteTail(Node* head){
        Node* temp=head;
        while(temp->next->next!=NULL){
            temp=temp->next;
        }
        Node* dlt=temp->next;
        temp->next=NULL;
        delete(dlt);
        return head;
    }
};

int main(){
    vector<int>arr={12,13,1,3,5};
    Insertion it;
    Node* head = it.arrToLL(arr);
    // cout<<head->data;
    head=it.insertAtHead(head,5);
    it.print(head);
    cout<<endl;
    head=it.insertAtTail(head,10);
    it.print(head);
    cout<<endl;
    head=it.insertATKthPos(head,3,45);
    it.print(head);
       cout<<endl;
    Deletion dt;
    head=dt.deleteHead(head);
    it.print(head);
    cout<<endl;
    head=dt.deleteTail(head);
    it.print(head);

}