# 题目描述
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        left = self.Convert(pRootOfTree.left)
        p = left

        while left and p.right:
            p = p.right

        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        right = self.Convert(pRootOfTree.right)

        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree

        return left if left else pRootOfTree

    def Convert2(self, pRootOfTree):
        if not pRootOfTree:
            return None

        stack =[]
        resstack = []

        p = pRootOfTree
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                resstack.append(node)
                p = node.right


        head = resstack[0]

        while resstack:
            top = resstack.pop(0)
            if resstack:
                top.right = resstack[0]
                resstack[0].left = top

        return head


