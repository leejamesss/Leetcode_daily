class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) { // 若操作数组为空，则全部为 0 的矩阵中最大整数的个数就是 m*n
            return m * n;
        }
        int minRow = m;
        int minCol = n;
        for (int[] op : ops) { // 遍历操作数组
            minRow = Math.min(minRow, op[0]); // 获取行操作的最小值
            minCol = Math.min(minCol, op[1]); // 获取列操作的最小值
        }
        return minRow * minCol; // 最大整数的个数就是最终矩阵中的元素的数量，即最终矩阵大小
    }
}
https://leetcode.cn/problems/range-addition-ii/
