# 题目描述
# 输入一个链表，反转链表后，输出新链表的表头。

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self,pHead):
        reverseHead = None
        pNode = pHead
        pPrev = None

        while pNode != None:
            pNext = pNode.next

            if pNext == None:
                reverseHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return reverseHead

    def ReverseListRec(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        reverseHead = self.ReverseList(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return reverseHead
