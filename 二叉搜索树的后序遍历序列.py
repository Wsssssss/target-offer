# 题目描述
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        root = sequence[-1]
        length = len(sequence)
        index = 0
        if min(sequence) > root and max(sequence) < root:
            return True

        for i in range(length - 1):
            index = i
            if sequence[i] > root:
                break

        for i in range(index + 1, length - 1):
            if sequence[i] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        right = True
        if index < length - 1:
            right = self.VerifySquenceOfBST(sequence[index:length - 1])

        return left and right
