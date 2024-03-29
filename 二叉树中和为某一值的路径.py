# 题目描述
# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        a, b = [],[]
        def subfindpath(root):
            if root:
                b.append(root.val)
                if root.left ==None and root.right == None and sum(b) ==expectNumber:
                    a.append(b[:])
                else:
                    subfindpath(root.left),subfindpath(root.right)
                b.pop()
        subfindpath(root)
        return a