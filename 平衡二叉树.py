# 题目描述
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

class Solution:
    def __init__(self):
        self.flag = True



    def IsBalanced_Solution(self, pRoot):
        self.getdepth(pRoot)
        return self.flag

    def getdepth(self,pRoot):
        if pRoot ==None:
            return 0
        left = self.getdepth(pRoot.left)+1
        right = self.getdepth(pRoot.right)+1

        if abs(left-right)>1:
            self.flag=False

        return left if left>right else right