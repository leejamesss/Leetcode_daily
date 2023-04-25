#https://leetcode.cn/problems/reverse-linked-list-ii/submissions/
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 遍历到 left - 1 结点
        for i in range(left-1):
            prev = prev.next
            
        cur = prev.next
        for i in range(right-left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next
