public class Solution {
    private final int MOD = 1337;

    public int superPow(int a, int[] b) {
        if (b.length == 0) return 1;

        int lastDigit = b[b.length - 1];
        int[] newB = new int[b.length - 1];
        System.arraycopy(b, 0, newB, 0, b.length - 1);

        int part1 = myPow(a, lastDigit);
        int part2 = myPow(superPow(a, newB), 10);

        return (part1 * part2) % MOD;
    }

    private int myPow(int a, int k) {
        a %= MOD;
        int result = 1;
        for (int i = 0; i < k; i++) {
            result = (result * a) % MOD;
        }
        return result;
    }
}

// https://leetcode.cn/problems/super-pow/submissions/
