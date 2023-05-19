

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        odd = cur_odd = head
        even = cur_even = head.next

        while cur_even and cur_even.next:
            cur_odd.next = cur_even.next  # 奇数链表连接到下一个奇数节点
            cur_odd = cur_odd.next
            cur_even.next = cur_odd.next  # 偶数链表连接到下一个偶数节点
            cur_even = cur_even.next

        cur_odd.next = even  # 将偶数链表接到奇数链表尾部

        return odd

# https://leetcode.cn/problems/odd-even-linked-list/submissions/
