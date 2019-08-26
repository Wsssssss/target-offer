# 题目描述
# 输入两个链表，找出它们的第一个公共结点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1length = self.length(pHead1)
        p2length = self.length(pHead2)

        lengthdiff = abs(p1length - p2length)

        if p1length > p2length:
            pHeadlong = pHead1
            pHeadshort = pHead2
        else:
            pHeadlong = pHead2
            pHeadshort = pHead1

        for i in range(lengthdiff):
            pHeadlong = pHeadlong.next

        while pHeadlong != None and pHeadshort != None and pHeadlong != pHeadshort:
            pHeadlong = pHeadlong.next
            pHeadshort = pHeadshort.next

        return pHeadlong

    def length(self, head):
        length = 0
        while head != None:
            head = head.next
            length += 1
        return length
