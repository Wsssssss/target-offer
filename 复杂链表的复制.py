# 题目描述
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead ==None:
            return None
        self.clonenode(pHead)
        self.connetclone(pHead)
        return self.connect(pHead)


    def clonenode(self,pHead):
        pNode = pHead
        while pNode:
            clonenode = RandomListNode(0)
            clonenode.label = pNode.label
            clonenode.next = pNode.next
            pNode.next = clonenode
            pNode = clonenode.next


    def connetclone(self,pHead):
        pNode = pHead
        while pNode:
            clonenode = pNode.next
            if pNode.random!=None:
                clonenode.random = pNode.random.next
            pNode = clonenode.next


    def connect(self,pHead):
        pNode = pHead
        cloneHead = clonenode = pNode.next
        pNode.next = cloneHead.next
        pNode = pNode.next
        while pNode:
            clonenode.next = pNode.next
            clonenode = clonenode.next
            pNode.next = clonenode.next
            pNode = pNode.next

        return cloneHead
