#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    //constructor
    Node(int data){
        this->data=data;
        this->next=NULL;
    }
    //destructor
    //for memory free;
    // ~Node(){
    //     int value=this->next;
    //     if(this->next!=NULL){
    //         delete next;
    //         this->next=NULL;
    //     }
    //     cout<<"memory is free for node with data "<<value<<endl;
    // }
};

void insertathead(Node* &head,int d){
    //create new node
    Node* temp=new Node(d);
    temp->next=head;
    head=temp;
}
void insertattail(Node* &tail,int d){
    Node* temp=new Node(d);
    tail->next=temp;
    tail=temp;
}
void insertatposition(Node* &head,Node* &tail,int position,int d){
    if(position==1){
        insertathead(head,d);
        return;
    }
    else{
        Node* temp=head;
        int count=1;
        while(count<position-1){
            temp=temp->next;
            count++;
        }
        //inserting at last position
        if(temp->next==NULL){
            insertattail(tail,d);
            return;
        }
        Node* nodetoinsert=new Node(d);
        nodetoinsert->next=temp->next;
        temp->next=nodetoinsert;   
    }
}
void deletenode(Node* &head,int position){
    if(position==1){
        Node* temp=head;
        head=head->next;
        temp->next=NULL;
        delete temp;
    }
    else{
        Node* curr=head;
        Node* prev=NULL;

        int count=1;
        while(count<=position){
            prev=curr;
            curr=curr->next;
            count++;
        }
        prev->next=curr->next;
        curr->next=NULL;
        delete curr;
    }
}
void Print(Node* &head){
    Node* temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}
int main(){
    Node* node1=new Node(10);
    //cout<<node1->data;
    Node* head=node1;
    Node* tail=node1;
    //insertathead(head,12);
    Print(head);
    insertattail(tail,12);
    insertatposition(head,tail,3,22);
    Print(head);
    cout<<head->data<<endl<<tail->data<<endl;
    deletenode(head,1);
    Print(head);
}