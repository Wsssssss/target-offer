# 题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root

        pre = root.left
        root.left = root.right
        root.right = pre

        self.Mirror(root.left)
        self.Mirror(root.right)