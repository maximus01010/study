#include<bits/stdc++.h>
using namespace std;

int binarysort(int nums[], int size,int x){
    int low=0;
    int high=size-1;
    while(low<=high){
         int mid = low + (high - low) / 2;
        if(nums[mid]==x){
            return mid;
        }
        if(x>nums[mid]){
            low=mid+1;
            
        }
        else{
            high=mid-1;
        }
    }
    return -1;
}

int main(){
    int nums[]={2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 7, 4, 2};
    int size = sizeof(nums) / sizeof(nums[0]); 
    sort(begin(nums),end(nums));

    cout<<binarysort(nums, size,2);
}
