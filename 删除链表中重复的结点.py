# 题目描述
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return
        preHead = None
        pNode = pHead
        while pNode != None:
            needdelete = False
            nextnode = pNode.next
            if nextnode != None and nextnode.val == pNode.val:
                needdelete = True
            if needdelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                nodeval = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == nodeval:
                    pToBeDel = pToBeDel.next
                if preHead == None:
                    preHead = pToBeDel
                    pNode = pToBeDel
                    continue
                else:
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead
