# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        queue = []
        if not root:
            return []
        result = []
        queue.append(root)
        while len(queue) > 0:
            currentroot = queue.pop(0)
            result.append(currentroot.val)
            if currentroot.left:
                queue.append(currentroot.left)
            if currentroot.right:
                queue.append(currentroot.right)

        return result