# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next

        return l
