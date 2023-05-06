#https://leetcode.cn/problems/copy-list-with-random-pointer/submissions/
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # 在每个节点后插入一个新节点
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        
        # 更新新节点的 random 指针
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        # 将拼接后的链表分离为两个链表，并返回新链表的头节点
        dummy = Node(0)
        p1, p2, cur = head, dummy, None
        while p1:
            p2.next = p1.next
            p2 = p2.next
            p1.next = p1.next.next
            p1 = p1.next
        
        return dummy.next
