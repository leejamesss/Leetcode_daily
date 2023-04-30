# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/submissions/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = root
        while cur:
            dummy = Node(-1)
            prev, nxt = dummy, None
            while cur:
                if cur.left:
                    prev.next, prev = cur.left, cur.left  # 更新 prev 的 next 指针
                    if cur.right:
                        prev.next, prev = cur.right, cur.right  # 同时更新右子节点
                elif cur.right:
                    prev.next, prev = cur.right, cur.right
                cur = cur.next
            cur = dummy.next  # 前往下一层的第一个节点

        return root
