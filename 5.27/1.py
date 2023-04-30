# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/submissions/
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if i < size - 1:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root
      
      
