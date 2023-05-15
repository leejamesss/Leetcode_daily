# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right        
 
