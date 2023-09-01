class Solution {
    private int[] prefixSum;
    private int n;

    public Solution(int[] w) {
        n = w.length;
        prefixSum = new int[n];

        prefixSum[0] = w[0];
        for (int i = 1; i < n; ++i) {
            prefixSum[i] = prefixSum[i - 1] + w[i];
        }
    }

    public int pickIndex() {
        int rand = (int) (Math.random() * prefixSum[n - 1]) + 1;
        int left = 0, right = n - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (prefixSum[mid] < rand) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
// https://leetcode.cn/problems/cuyjEf/submissions/
