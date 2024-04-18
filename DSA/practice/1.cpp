#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int>v={3,3,4,1,1,1,2,3};
    map<int,int>m;
    for(int i=0;i<v.size();i++){
        m[v[i]]=m[v[i]]+1;
    }
    for(int i=v.size()-1;i>=0;i--){
        if(m[v[i]]>=v[i]){
            cout<<v[i];
        }
    }
}