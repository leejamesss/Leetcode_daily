class Solution {
    public int minSteps(int n) {
        if (n == 1) {
            return 0;
        }
        
        int[] dp = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            dp[i] = i; // 最坏情况下的初始值，即全部由复制和粘贴操作构成
            for (int j = i - 1; j > 1; j--) {
                if (i % j == 0) {
                    dp[i] = dp[j] + (i / j);
                    break;
                }
            }
        }
        
        return dp[n];
    }
}
https://leetcode.cn/problems/2-keys-keyboard/
