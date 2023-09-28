// https://leetcode.cn/problems/binary-search/
class Solution {
    public int search (int[] nums,int target){
        if ((target<nums[0]) || (target>nums[nums.length-1])) {
            return -1;
        }

        int left=0;
        int right=nums.length-1;
        while (left<=right){
            int mid = left+((right-left)>>1);
            if (target==nums[mid]){
                return mid;
            }
            else if (target > nums[mid]){
                left=mid+1;
            }
            else if (target < nums[mid]){
                right=mid-1;
            }

        }   
        return -1;

    }

}
