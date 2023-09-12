class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        } else {
            dfs(root, val, depth, 1);
            return root;
        }
    }

    private void dfs(TreeNode node, int val, int depth, int currentDepth) {
        if (node == null) {
            return;
        }
        if (currentDepth == depth - 1) {
            TreeNode newLeft = new TreeNode(val);
            TreeNode newRight = new TreeNode(val);
            newLeft.left = node.left;
            newRight.right = node.right;
            node.left = newLeft;
            node.right = newRight;
        } else {
            dfs(node.left, val, depth, currentDepth + 1);
            dfs(node.right, val, depth, currentDepth + 1);
        }
    }
}

https://leetcode.cn/problems/add-one-row-to-tree/
