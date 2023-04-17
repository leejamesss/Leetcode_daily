# https://leetcode.cn/problems/swap-nodes-in-pairs/
#递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextHead = self.swapPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = nextHead
        return newHead
#对以 head 为头节点的链表进行两两交换

#分为两部分，第一部分是前两个节点，第二部分是剩余的节点
#递归调用 swapPairs 函数对剩余部分进行两两交换
#得到新的头节点 newHead
#前两个节点进行交换
#将它们和新的头节点连接起来。最后返回新的头节点
