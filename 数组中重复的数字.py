# 题目描述
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers == None or len(numbers)<1:
            return False
        for i in numbers:
            if i<0 or i> len(numbers)-1:
                return False

        for i in range(len(numbers)):
            while numbers[i]!=i:
                if numbers[i]==numbers[numbers[i]]:
                    duplication[0]=numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i],numbers[index]=numbers[index],numbers[i]

        return False