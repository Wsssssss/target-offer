# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        Hhead = head
        Hbehind = None

        for i in range(k - 1):
            if Hhead.next != None:
                Hhead = Hhead.next
            else:
                return None
        Hbehind = head
        while Hhead.next != None:
            Hhead = Hhead.next
            Hbehind = Hbehind.next
        return Hbehind
