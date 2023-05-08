# https://leetcode.cn/problems/insertion-sort-list/
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 定义 dummy 节点
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = head.next

        while cur:
            # 如果当前节点比前一个节点大，就不需要移动。
            if cur.val >= pre.val:
                pre = cur
                cur = cur.next
                continue

            # 从头开始遍历已排序的链表部分
            pre.next = cur.next
            p = dummy
            while cur.val > p.next.val:
                p = p.next
            # 插入 cur 节点
            cur.next = p.next
            p.next = cur
            # 移动 cur 指针
            cur = pre.next

        return dummy.next
