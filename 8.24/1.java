class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return buildTree(nums, 0, nums.length - 1);
    }
    
    private TreeNode buildTree(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        
        int maxIdx = findMaxIndex(nums, start, end); // 找到当前范围内的最大值的索引
        TreeNode root = new TreeNode(nums[maxIdx]); // 创建根节点
        
        root.left = buildTree(nums, start, maxIdx - 1); // 构建左子树
        root.right = buildTree(nums, maxIdx + 1, end); // 构建右子树
        
        return root;
    }
    
    private int findMaxIndex(int[] nums, int start, int end) {
        int maxIdx = start;
        for (int i = start + 1; i <= end; i++) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }
        return maxIdx;
    }
}
https://leetcode.cn/problems/maximum-binary-tree/
