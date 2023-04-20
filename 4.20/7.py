# https://leetcode.cn/problems/rotate-list/submissions/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k == 0:
            return head
        new_tail = head
        for i in range(length-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head

# 测试代码
def printList(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print('NULL')

if __name__ == '__main__':
    # Testcase 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    k = 2
    printList(l1)
    sol = Solution()
    res = sol.rotateRight(l1, k)
    printList(res)
    # expected output: 4->5->1->2->3->NULL
    
    # Testcase 2
    l2 = ListNode(0)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    k = 4
    printList(l2)
    sol = Solution()
    res = sol.rotateRight(l2, k)
    printList(res)
    # expected output: 2->0->1->NULL
