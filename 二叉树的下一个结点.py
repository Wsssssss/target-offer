# 题目描述
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        pNext = None

        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode
        else:
            if pNode.next and pNode == pNode.next.left:
                pNext = pNode.next

            elif pNode.next and pNode == pNode.next.right:
                pNode = pNode.next
                while pNode.next and pNode == pNode.next.right:
                    pNode = pNode.next
                if pNode.next:
                    pNext = pNode.next

        return pNext