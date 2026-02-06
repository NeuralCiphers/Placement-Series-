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
int  print(Node* head){
    Node* temp=head;
    int cnt=0;
    while(temp!=NULL){
        cnt++;
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    return cnt;
}
int main(){
    vector<int>arr={12,13,1,3,5};
    Node* head = arrToLL(arr);
    // cout<<head->data;
    int cnt=print(head);
    cout<<endl<<"Total number of nodes :"<<cnt;
}