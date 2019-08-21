# 题目描述
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        if numbers == None or length <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

    def CheckMoreThanHalf(self, numbers, length, result):
        time = 0
        for i in range(length):
            if result == numbers[i]:
                time += 1
        if time * 2 <= length:
            return False
        return True
