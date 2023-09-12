class Solution {
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root); // 计算树的高度
        int width = (int) Math.pow(2, height) - 1; // 计算矩阵的宽度
        List<List<String>> res = new ArrayList<>();
        for (int i = 0; i < height; i++) {
            List<String> row = new ArrayList<>();
            for (int j = 0; j < width; j++) {
                row.add("");
            }
            res.add(row);
        }
        fillMatrix(res, root, 0, 0, width - 1);
        return res;
    }
    
    private int getHeight(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
    }
    
    private void fillMatrix(List<List<String>> res, TreeNode node, int row, int left, int right) {
        if (node == null) {
            return;
        }
        
        int mid = left + (right - left) / 2;
        res.get(row).set(mid, String.valueOf(node.val));
        
        fillMatrix(res, node.left, row + 1, left, mid - 1); // 左子节点在下一行的左边
        fillMatrix(res, node.right, row + 1, mid + 1, right); // 右子节点在下一行的右边
    }
}
https://leetcode.cn/problems/print-binary-tree/
