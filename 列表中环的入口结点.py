# 题目描述
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow, fast = pHead, pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = pHead
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow
