#include<bits/stdc++.h>
using namespace std;
class Node{
    public:
    int data;
    Node* prev;
    Node* next;
    //constructor
    Node(int d){
        this->data=d;
        this->next=NULL;
        this->prev=NULL;
    }
    ~Node(){
        int val=this->data;
        if(next!=NULL){
            delete next;
            next=NULL;
        }
    }
};
void insertathead(Node* &head,int d){
    Node* temp=new Node(d);
    temp->next=head;
    head->prev=temp;
    head=temp;
}
void insertattail(Node* &tail,int d){
    Node* temp=new Node(d);
    tail->next=temp;
    temp->prev=tail;
    tail=temp;
}
void insertatanyposition(Node* &head,Node* &tail,int positon,int d){
    if(positon==1){
        insertathead(head,d);
        return;
    }
    else{
        Node* temp=head;
        int count=1;
        while(count<positon-1){
            temp=temp->next;
            count++;
        }
        if(temp->next==NULL){
            insertattail(tail,d);
            return;
        }
        Node* nodetoinsert=new Node(d);
        nodetoinsert->next=temp->next;
        nodetoinsert->next->prev=nodetoinsert;
        temp->next=nodetoinsert;
        nodetoinsert->prev=temp;

    }
}
void deletenode(Node* &head,int position){
    if(position==1){
        Node* temp=head;
        head->next->prev=NULL;
        head=temp->next;
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
        curr->prev=NULL;
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
void getlength(Node* &head){
    Node* temp=head;
    int len=0;
    while(temp!=NULL){
        len++;
        temp=temp->next;
    }
    cout<<"lenght="<<len<<endl;
}
int main(){
    Node* node1=new Node(10);
    Node* head=node1;
    Node* tail=node1;
    Print(head);
    getlength(head);
    insertathead(head,22);
    Print(head);
    insertattail(tail,19);
    Print(head);
    insertatanyposition(head,tail,1,100);
    Print(head);
    //deletenode(head,4);
    //Print(head);
}