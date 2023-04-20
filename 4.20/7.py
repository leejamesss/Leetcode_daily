# https://leetcode.cn/problems/rotate-list/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        # 遍历一遍链表，求出链表长度
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        # 对 k 进行取模
        k = k % length
        if k == 0:
            return head
        # 找到倒数第 k' 个结点，以及它前面的那个结点
        last = head
        for i in range(length - k - 1):
            last = last.next
        new_head = last.next
        # 拆掉 last 和 new_head 之间的链接，并让链表尾部接到链表头部
        last.next = None
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
