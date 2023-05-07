# https://leetcode.cn/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 定义快指针和慢指针，并起始指向头节点
        fast = slow = head
        # 判断是否存在环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 如果存在环，则从头节点和相遇点同时开始移动，直到相遇为止
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        # 如果不存在环，则返回null
        return None

