class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 处理链表为空的情况
        if not head:
            return None
        
        # 处理头节点就是需要删除的节点的情况
        while head and head.val == val:
            head = head.next
        
        # 处理中间某个节点是需要删除的节点的情况
        prev, cur = None, head
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next
        
        return head

# https://leetcode.cn/problems/remove-linked-list-elements/submissions/
