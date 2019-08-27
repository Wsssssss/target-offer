# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0:
            return []

        length = len(array)
        left = 0
        right = length-1

        while left < right:
            sum = array[left] + array[right]
            if sum == tsum:
                return [array[left], array[right]]
            elif sum<tsum:
                left+=1
            else:
                right-=1

        return []