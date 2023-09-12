class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>(); // 使用队列来进行 BFS
        queue.offer(new Pair<>(root, 0)); // 将根节点入队
        
        int maxWidth = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            int left = queue.peek().getValue(); // 当前层的最左边节点的位置
            int right = left; // 当前层的最右边节点的位置
            
            for (int i = 0; i < size; i++) {
                Pair<TreeNode, Integer> pair = queue.poll();
                TreeNode node = pair.getKey();
                int position = pair.getValue();
                
                right = position; // 更新最右边节点的位置
                
                // 将左右子节点入队，并记录它们的位置
                if (node.left != null) {
                    queue.offer(new Pair<>(node.left, position * 2));
                }
                if (node.right != null) {
                    queue.offer(new Pair<>(node.right, position * 2 + 1));
                }
            }
            
            // 计算当前层的宽度，并更新最大宽度
            int width = right - left + 1;
            maxWidth = Math.max(maxWidth, width);
        }
        
        return maxWidth;
    }
}
https://leetcode.cn/problems/maximum-width-of-binary-tree/
