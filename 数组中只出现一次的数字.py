# 题目描述
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []

        num = 0
        for i in array:
            num ^= i

        index = self.findindex(num)

        num1 = 0
        num2 = 0
        for j in range(len(array)):
            if self.index(array[j], index):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def findindex(self, num):
        index = 0
        while num & 1 == 0 and index < 32:
            index += 1
            num = num >> 1
        return index

    def index(self, number, index):
        number = number >> index
        return number & 1
