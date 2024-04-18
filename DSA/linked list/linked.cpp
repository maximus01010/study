#include<bits/stdc++.h>
using namespace std;
class node{
    public:
    int data;
    node* next;
    node(int data1){
        this->data=data1;
        this->next=NULL;
    }
};
void insertn(node* head,int data){
    node* datanode=new node(data);
    
}
int main(){
    node* head=new node(24);
    insertn(head,55);
    insertn(head,53);
}