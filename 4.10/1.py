#https://leetcode.cn/problems/reverse-nodes-in-k-group
#迭代



class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        prev = tail.next # 将尾部与后面的链表连接
        p = head
        while prev != tail:
            nextNode = p.next
            p.next = prev
            prev = p
            p = nextNode
        return tail, head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nextNode = tail.next # 下一个区间的头节点
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = nextNode
            prev = tail
            head = nextNode
        return dummy.next


      
