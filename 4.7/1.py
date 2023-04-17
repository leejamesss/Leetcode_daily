
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
#双指针
# 维护两个指针 p 和 q，初始时都指向链表的头结点

#让 q 往前移动 n 个节点
#然后让 p 和 q 同时往前移动，直到 q 到达链表的末尾
#此时 p 指向的就是倒数第 n+1 个节点，把它的 next 指针指向下一个节点的 next 指针即可。
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy
        for i in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        return dummy.next
