#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int>height={1,1};
    int left=0,right=height.size()-1;
    int ans=0;
    int area=abs(left-right)*(min(height[left],height[right]));
    for(int i=0;i<height.size();i++){
        if(height[right]>=height[left]){
            left++;
            area=max(abs(left-right)*(min(height[left],height[right])),area);
        }
    }
    cout<<area;
}