# 题目描述
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead ==None or pHead.next==None:
            return pHead
        new_head = ListNode(-1)
        new_head.next = pHead
        pre = new_head
        p = pHead
        next=None
        while p!=None and p.next!=None:
            next =p.next
            if p.val==next.val:
                while next!=None and p.val==next.val:
                    next=next.next
                pre.next = next
                p = next
            else:
                pre = p
                p = p.next
        return new_head.next