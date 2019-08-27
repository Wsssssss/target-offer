# 题目描述
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0

        treelist = []
        treelist.append(pRoot)
        depth = 0
        while len(treelist):
            treelen = len(treelist)
            while treelen:
                node = treelist.pop(0)
                treelen -= 1
                if node.left != None:
                    treelist.append(node.left)
                if node.right != None:
                    treelist.append(node.right)
            depth += 1
        return depth
