# 题目描述
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑|数。

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == None or index <= 0:
            return 0
        indexnumber = [1] * index
        nextindex = 1
        index2 = 0
        index3 = 0
        index5 = 0

        while nextindex < index:
            minval = min(indexnumber[index2] * 2, indexnumber[index3] * 3, indexnumber[index5] * 5)
            indexnumber[nextindex] = minval
            while indexnumber[index2] * 2 <= indexnumber[nextindex]:
                index2 += 1
            while indexnumber[index3] * 3 <= indexnumber[nextindex]:
                index3 += 1
            while indexnumber[index5] * 5 <= indexnumber[nextindex]:
                index5 += 1
            nextindex += 1

        return indexnumber[-1]
