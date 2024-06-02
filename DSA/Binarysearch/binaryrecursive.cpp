#include<bits/stdc++.h>
using namespace std;
int binarysearch(int nums[],int low,int high,int wanted){
    int mid=low+(high-low)/2;
    if(nums[mid]==wanted){
        return mid;
    }
    if(nums[mid]>wanted){
        return binarysearch(nums,low,mid-1,wanted);
    }
    else{
        return binarysearch(nums,mid+1,high,wanted);
    }
}
int main(){
    int nums[]={1,2,3,7,9,11,42,66};
    int wanted=66;
    int low=0;
    int high= (sizeof(nums) / sizeof(nums[0]))-1;
    cout<<binarysearch(nums,low,high,wanted); 

}