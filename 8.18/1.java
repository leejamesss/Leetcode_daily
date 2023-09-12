// https://leetcode.cn/problems/wiggle-subsequence/
public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        
        int maxLength = 1;
        
        int prevDiff = nums[1] - nums[0];
        if (prevDiff != 0) {
            maxLength = 2;
        }
        
        for (int i = 2; i < nums.length; i++) {
            int diff = nums[i] - nums[i-1];
            if ((diff > 0 && prevDiff <= 0) || (diff < 0 && prevDiff >= 0)) {
                maxLength++;
                prevDiff = diff;
            }
        }
        
        return maxLength;
    }
}
